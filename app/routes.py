#Python and flask libraries
from app import app
from flask import render_template
from flask import request
from flask import jsonify
from grandpy.grandpytalk import Grandpytalk

#Program libraries
from grandpy.grandpytalk import Grandpytalk

@app.route('/')
@app.route('/index')
def index():
    grandpy = Grandpytalk()
    hello_message = grandpy.intro_message()
    return render_template("/app/index.html", title="Grandpybot", hello_message=hello_message)

@app.route('/grandpytalk', methods=["POST"])
def grandpytalk():
    message = request.get_json()["text"]
    print("Debug : "+message)
    papy = Grandpytalk()
    answer = papy.ask_grandpy(message)

    return jsonify(answer)