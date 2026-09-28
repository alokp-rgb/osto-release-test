import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)

API_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyzAB"


@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    return subprocess.check_output("ping -c 1 " + host, shell=True)


@app.route("/user")
def user():
    uid = request.args.get("id", "")
    conn = sqlite3.connect("app.db")
    return conn.execute("SELECT * FROM users WHERE id = '" + uid + "'").fetchall()
