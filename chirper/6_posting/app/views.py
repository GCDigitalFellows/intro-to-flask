from flask import Flask, render_template, request, redirect, url_for
from app import app
import sqlite3
import datetime


# This lets us import dictionaries from the database instead of tuples
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route("/")
@app.route("/index")
def index():
    # This data is fake in the sense that we're just adding it here
    # Later we'll use a database for this

    # This is a list of dictionaries, they will be our chirp data

    conn = sqlite3.connect("chirper.db")
    conn.row_factory = dict_factory
    cur = conn.cursor()

    cur.execute("SELECT * FROM chirp;")
    chirps = cur.fetchall()

    # now we give our chirps data to the template so that it can be displayed
    return render_template('index.html', chirps=chirps)


@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/chirp", methods=["GET", "POST"])
def post_chirp():
    if request.method == 'POST':
        chirptext = request.form['chirptext']
        time = datetime.datetime.now()
        username = request.form['username']

        conn = sqlite3.connect("chirper.db")
        conn.row_factory = dict_factory
        cur = conn.cursor()
        cur.execute("INSERT INTO chirp (time, user, text) VALUES (?, ?, ?)",
                    (time, username, chirptext))
        conn.commit()
        return redirect(url_for("index"))


    return render_template("post_chirp.html")
