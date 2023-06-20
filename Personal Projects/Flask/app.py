import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    dt_time = datetime.datetime.utcnow()
    return render_template("index.html", dt_time=dt_time)
