import os

from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_bcrypt import generate_password_hash, check_password_hash
# from database import Users, House
from os import path
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.debug = True

@app.route('/', methods=["POST", "GET"])

def predictor():
    # if request.method == "POST":
    #     jina = request.form["x"]
    #     arafa = request.form["y"]
    #     siri = request.form["z"]
    #     encrypted_password = generate_password_hash(siri)
    #     Users.create(name=jina, email=arafa, password=encrypted_password)
    #     flash("User registered successfully")
    return render_template("predictor.html")


if __name__ == '__main__':
    app.run()
