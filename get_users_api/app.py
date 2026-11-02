#!/usr/bin/python
import sqlite3
from flask import Flask, jsonify


def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn


def get_user_names():
    names = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT name FROM users")
        rows = cur.fetchall()

        for i in rows:
            names.append(i["name"])

    except:
        names = []

    return names


app = Flask(__name__)


@app.route('/api/get_users', methods=['GET'])
def api_get_users():
    return jsonify(get_user_names())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
