from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config["SECRET_KEY"] = 'oh-so-secret'

debug = DebugToolbarExtension(app)


@app.route('/')
def show_form():

    word_list = story.prompts
    return render_template('index.html', prompts=word_list)


@app.route('/story')
def show_story():
    inputs = request.args
    story_text = story.generate(inputs)
    return render_template('story.html', story_text = story_text)
