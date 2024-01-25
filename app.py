from flask import Flask, render_template, request
from stories import stories_list

app = Flask(__name__)


@app.route("/")
def choose():
    return render_template("choose.html", stories_list = stories_list)

@app.route("/create")
def home_page():
    story_index = request.args.get("story_index", "0")

    story = stories_list[int(story_index)]
    prompts = story.prompts

    return render_template("create.html", prompts = prompts, story_index = story_index)



@app.route("/story",)
def story_submit():
    story_index = request.args.get("story_index", "0")
    story = stories_list[int(story_index)]

    data = dict(request.args)
    data.pop("story_index")
    story_text = story.generate(data)
    return render_template("story.html", story_text = story_text)