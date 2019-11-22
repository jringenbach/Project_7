#Python and flask libraries
from app import app
from flask import render_template

#Program libraries
from grandpy.grandpytalk import Grandpytalk

@app.route('/')
@app.route('/index')
def index():
    grandpy = Grandpytalk()
    hello_message = grandpy.intro_message()
    return render_template("/app/index.html", title="Grandpybot", hello_message=hello_message)