from flask import Blueprint, render_template, Response
import sqlite3
import re
from cairosvg import svg2png
from uuid import uuid4

DB = "counter.db"

view_counter = Blueprint("view_counter", __name__, static_folder='static')

uuid_validator = re.compile("(?P<uuid>[0-9a-f]{8}\-[0-9a-f]{4}\-4[0-9a-f]{3}\-[89ab][0-9a-f]{3}\-[0-9a-f]{12})")

def to_png(svg):
    return svg2png(svg.encode())

@view_counter.route("/counter/<uuid>")
def counter(uuid):
    if uuid_validator.fullmatch(uuid) is None:
        return "error uuid wrong"
    with sqlite3.connect(DB) as db:
        cursor = db.cursor()
        cursor.execute("INSERT OR IGNORE INTO counters (uuid, count) VALUES (?, 0)", (uuid,))
        cursor.execute("UPDATE counters SET count = count + 1 WHERE uuid = ?", (uuid,))
        result = cursor.execute("SELECT count FROM counters WHERE uuid = ?", (uuid,))
        result = list(result)
        count = result[0][0]
    return Response(to_png(render_template("base.svg", count = count)), mimetype="image/png")

@view_counter.route("/")
def index():
    return render_template("index.html", counter = str(uuid4()))
