"""
Portfolio

A Portfolio Site to showcase my work, implemented using GitHub Pages.


Author: Nick Foerster
Date: 01/08/24
"""

# IMPORTS
# ---------------
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from helpers import apology, login_required, query_val, uid_val, get_form_submissions


# Turn this file into a Flask Application
app = Flask(__name__)

# Configure session to use the filesystem
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    """Portfolio Main Page"""

    return render_template("index.html")

