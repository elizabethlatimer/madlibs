from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import trad_fairytale, modern_fairytale, punk_fairytale, sad_fairytale

app = Flask(__name__)
app.config["SECRET_KEY"] = 'oh-so-secret'

debug = DebugToolbarExtension(app)
STORY_LIST = [trad_fairytale, modern_fairytale, punk_fairytale, sad_fairytale]

@app.route("/")
def pick_story():
    return render_template('index.html', story_list = STORY_LIST)

@app.route('/inputs')
def show_form():
    chosen_story = request.args["story_choice"]
    for story in STORY_LIST:
        if chosen_story == story.title:
            word_list = story.prompts
    return render_template('inputs.html', prompts=word_list, chosen_story=chosen_story)


@app.route('/story')
def show_story():
    inputs = request.args
    for story in STORY_LIST:
        if inputs['story_input'] == story.title:
            story_text = story.generate(inputs)
    return render_template('story.html', story_text = story_text)
