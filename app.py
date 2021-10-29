from flask import Flask, session, redirect, url_for, escape, request, jsonify, render_template
from dungeon import dungeon_map
from multiprocessing import Value

game_map = dungeon_map
app = Flask(__name__)
app.secret_key = 'game_map'
counter = Value('i', 0)
counter.value += 1

@app.route("/")
def index():
    session['room_name'] = game_map.START
    return redirect(url_for("game"))

@app.route("/game", methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')
    
    if request.method == "GET":

        if room_name and counter.value < 4:
            room = game_map.load_room(room_name)
            return render_template("show_room.html", room=room, counter=counter)
        else:
            counter.value = 1
            return render_template("you_died.html")

    else:
        action = request.form.get('action')
        if room_name and action:
            room = game_map.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                with counter.get_lock():
                    counter.value += 1
                    out = counter.value
                session['room_name'] = game_map.name_room(room)
            else:
                counter.value = 1
                out = counter.value
                print(out)
                session['room_name'] = game_map.name_room(next_room)
        return redirect(url_for("game"))

@app.route('/hello')
def hello():
    return "hello"

@app.route('/count')
def make_count():
    with counter.get_lock():
        counter.value += 1
        out = counter.value

    return jsonify(count=out)

if __name__ == "__main__":
    app.run()

## ToDo:
# - add math.isclose(a, b, rel_tol=1e-5) to allow division
# - format HTML/CSS
# - actually make the game
# - secret path?