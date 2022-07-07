#!/usr/bin/env python3
from flask import Flask, redirect, render_template, request, url_for, jsonify
import requests
app = Flask(__name__)

no = {"reason": "I don't like him either"}


@app.route("/no")
def index():
    # return json
    return jsonify(no)


URL = "https://api.kanye.rest/"
# Create a variable for the JSON data from the API
resp = requests.get(URL).json()


@app.route("/")
def start():
    return render_template("kanye.html")


@app.route("/kanye")
def kanye():
    # Return the JSON data from the API
    return resp


@app.route("/why")
def why():
    return f"Good choice"


@app.route("/read", methods=["POST", "GET"])
def read():
    if request.form.get("yes"):
        # redirect to the kanye page
        return redirect(url_for("kanye"))
    else:
        return redirect(url_for("why"))


@app.route("/quote/<string:choice>")
def hello_name(choice):
    return render_template("quote.html", choice=choice)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
