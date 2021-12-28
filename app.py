from flask import Flask, session, redirect, url_for, escape, request, jsonify, render_template
from datetime import datetime
import re
from waterloo import waterloo_map
from multiprocessing import Value

game_map = waterloo_map
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

        if room_name: 
            room = game_map.load_room(room_name)
            if counter.value > room.limit:
                counter.value = 1
                room = game_map.load_room(room_name + '_fail')
            return render_template("show_room.html", room=room, counter=counter)

    else:
        action = request.form.get('action')
        if room_name:
            room = game_map.load_room(room_name)
            next_room = room.go(action)
            if not next_room:
                with counter.get_lock():
                    counter.value += 1
                session['room_name'] = game_map.name_room(room)
            else:
                counter.value = 1
                session['room_name'] = game_map.name_room(next_room)
        return redirect(url_for("game"))


@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content


@app.route('/count')
def make_count():
    with counter.get_lock():
        counter.value += 1
        out = counter.value

    return jsonify(count=out)

if __name__ == "__main__":
    app.run()