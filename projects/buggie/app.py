"""
Buggie - A Bug Tracker

This is a simple bug tracker.
The goal is to make tracking your projects second nature,
and an invisible part of your workflow, as a solo developer.


Author: Nick Foerster
Date: 12/22/23
"""

# IMPORTS
# ---------------
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, query_val, uid_val, get_form_submissions


# Turn this file into a Flask Application
app = Flask(__name__)

# Configure session to use the filesystem
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use the buggie.db database (sqlite)
db = SQL("sqlite:///buggie.db")


@app.route("/")
@login_required
def index():
    """Display Summary of Projects
    Allow for creation of Projects"""

    # Use helper function to retrieve currently logged in user id
    user_id = uid_val()

    # Select all rows from the table
    projects_list = db.execute("SELECT * FROM projects WHERE user_id = ?", user_id)

    return render_template("index.html", projects_list=projects_list)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register for an Account"""

    if request.method == "POST":
        # USER INPUT
        # ----------------

        # Request a username from the user
        name = request.form.get("username")

        # Request a password from the user
        password = request.form.get("password")

        # Request a password confirmation from the user
        confirmation = request.form.get("confirmation")

        # Query database for the provided username
        rows = db.execute("SELECT * FROM users WHERE username = ?", name)

        # VALIDATIONS
        # ----------------

        # Ensure name is not empty
        if name == "":
            return apology("Name provided was empty!")

        # Ensure the given username doesn't already exist in the db
        if len(rows) != 0:
            return apology("Username already registered!")

        # Ensure password is not empty
        if password == "":
            return apology("Password provided was empty!")

        # Ensure confirmation is not empty
        if confirmation == "":
            return apology("Password confirmation provided was empty!")

        # Ensure password and confirmation match
        if password != confirmation:
            return apology("Password and confirmation do not match!")

        # PASSWORD FORMAT VERIFICATION
        # ----------------

        # Make some handy variables for password verification
        pass_length = len(password)
        contains_uppers = 0
        contains_lowers = 0
        contains_numerals = 0
        contains_special_chars = 0

        # List of special characters to be used in password
        special_chars = ["!", "@", "#", "$", "%", "^", "&", "*"]

        # Loop through the password, checking for each type
        for s in password:
            if s.isupper():
                contains_uppers += 1
            elif s.islower():
                contains_lowers += 1
            elif s.isnumeric():
                contains_numerals += 1
            elif s in special_chars:
                contains_special_chars += 1

        # Final password validation
        if (
            pass_length < 12
            or contains_uppers == 0
            or contains_lowers == 0
            or contains_numerals == 0
            or contains_special_chars == 0
        ):
            return apology("Password does not satisfy requirements!")

        # SERVER UPDATES
        # ----------------

        # Create a hash of the password
        hash = generate_password_hash(password)

        # Ensure the hashing function was successful
        if not hash:
            return apology("Error hashing password", 500)

        # Input the submitted information into the users db
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", name, hash)

        # Add the stored hash to a variable
        stored_hash = query_val(
            db.execute("SELECT hash FROM users WHERE username = ?", name), "hash"
        )

        # I want to double check the hash created and stored is correct.
        if not check_password_hash(stored_hash, password):
            return apology("Error hashing password", 500)

        # Remember the session for this user, so they stay logged in
        # Select the user id from the db
        user_id = db.execute("SELECT id FROM users WHERE username = ?", name)

        # If the user_id exists, add to the session
        if user_id:
            session["user_id"] = user_id[0]["id"]

        return redirect("/")

    else:
        return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    """Login to an Account"""

    # Clear the current session to logout any user logged in
    session.clear()

    if request.method == "POST":
        # USER INPUT
        # ----------------

        # Request a username from the user
        name = request.form.get("username")

        # Request a password from the user
        password = request.form.get("password")

        # Query database for the provided username
        rows = db.execute("SELECT * FROM users WHERE username = ?", name)


        # VALIDATIONS
        # ----------------

        # Ensure name is not empty
        if not name or name == "":
            return apology("Name provided was empty!")

        # Ensure password is not empty
        if not password or password == "":
            return apology("Password provided was empty!")

        # Ensure username is correct
        if len(rows) != 1:
            return apology("Invalid username and/or password!")

        # Ensure password is correct
        if not check_password_hash(rows[0]["hash"], password):
            return apology("Invalid username and/or password!")

        # ----------------

        # Remember the user that logged in
        session["user_id"] = rows[0]["id"]

        # Redirect the user to the homepage
        return redirect("/")

    else:
        return render_template("login.html")



@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



# Passing <int:project_id> was learned from the following source:
# https://www.geeksforgeeks.org/passing-url-arguments-in-flask/
@app.route("/project/<int:project_id>", methods=["GET"])
@login_required
def project(project_id):
    """Show statuses of bugs for individual features"""

    # Then, select all the features associated with that project
    features_list = db.execute("SELECT * FROM features WHERE project_id = ?", project_id)

    # Only then do we render template
    return render_template("project.html", features_list=features_list, project_id=project_id)



@app.route("/addproject", methods=["POST"])
@login_required
def addproject():
    """Adds a Project to the projects table"""

    # Use my helper function to retrieve currently logged in user id
    user_id = uid_val()

    # Use my helper function to get form submissions, check they aren't empty, and return a dict with the results
    dict = get_form_submissions(2)

    # Add to the projects table
    db.execute("INSERT INTO projects (user_id, title, summary) VALUES (?, ?, ?)", user_id, dict["title"], dict["summary"])

    return redirect("/")


@app.route("/editproject/<int:project_id>", methods=["POST"])
@login_required
def editproject(project_id):
    """Edits a Project in the projects table"""

    # Use my helper function to get form submissions, check they aren't empty, and return a dict with the results
    dict = get_form_submissions(2)

    # Add to the projects table
    db.execute("UPDATE projects SET title = ?, summary = ? WHERE id = ?", dict["title"], dict["summary"], project_id)

    return redirect("/")



@app.route("/deleteproject/<int:project_id>", methods=["GET"])
@login_required
def deleteproject(project_id):
    """Deletes a Project in the projects table"""

    # Delete from the projects table
    db.execute("DELETE FROM projects WHERE id = ?", project_id)

    return redirect("/")



@app.route("/feature/<int:feature_id>", methods=["GET"])
@login_required
def feature(feature_id):
    """Shows kanban board with bugs from selected feature"""

    # Then, select all the features associated with that project
    bugs_list = db.execute("SELECT * FROM bugs WHERE feature_id = ?", feature_id)

    # Find the feature name, to display as the title of the page
    feature_name = query_val(db.execute("SELECT title FROM features WHERE id = ?", feature_id), "title")

    # Find the project id, to be used in the breadcrumb navigation on the feature page
    project_id = query_val(db.execute("SELECT project_id FROM features WHERE id = ?", feature_id), "project_id")

    # Only then do we render template
    return render_template("feature.html", bugs_list=bugs_list, feature_name=feature_name, feature_id=feature_id, project_id=project_id)



@app.route("/addfeature/<int:project_id>", methods=["POST"])
@login_required
def addfeature(project_id):
    """Adds a Feature to the Projects table"""

    # Use my helper function to get form submissions, check they aren't empty, and return a dict with the results
    dict = get_form_submissions(2)

    # Add to the features table
    db.execute("INSERT INTO features (project_id, title, summary) VALUES (?, ?, ?)", project_id, dict["title"], dict["summary"])

    return redirect("/project/" + str(project_id))



@app.route("/editfeature/<int:project_id>/<int:feature_id>", methods=["POST"])
@login_required
def editfeature(project_id, feature_id):
    """Edits a Feature in the features table"""

    # Use my helper function to get form submissions, check they aren't empty, and return a dict with the results
    dict = get_form_submissions(2)

    # Add to the projects table
    db.execute("UPDATE features SET title = ?, summary = ? WHERE id = ?", dict["title"], dict["summary"], feature_id)

    return redirect("/project/" + str(project_id))



@app.route("/deletefeature/<int:project_id>/<int:feature_id>", methods=["GET"])
@login_required
def deletefeature(project_id, feature_id):
    """Deletes a Project in the projects table"""

    # Delete from the projects table
    db.execute("DELETE FROM features WHERE id = ?", feature_id)

    return redirect("/project/" + str(project_id))



@app.route("/addbug/<int:feature_id>", methods=["POST"])
@login_required
def addbug(feature_id):
    """Adds a Bug to the Features table"""

    # Use my helper function to get form submissions, check they aren't empty, and return a dict with the results
    dict = get_form_submissions(4)

    # Add to the bugs table
    db.execute("INSERT INTO bugs (feature_id, title, summary, severity, state) VALUES (?, ?, ?, ?, ?)", feature_id, dict["title"], dict["summary"], dict["severity"], dict["state"])

    return redirect("/feature/" + str(feature_id))



@app.route("/editbug/<int:feature_id>/<int:bug_id>", methods=["POST"])
@login_required
def editbug(feature_id, bug_id):
    """Edits a Feature in the features table"""

    # Use my helper function to get form submissions, check they aren't empty, and return a dict with the results
    dict = get_form_submissions(4)

    # Add to the projects table
    db.execute("UPDATE bugs SET title = ?, summary = ?, severity = ?, state = ? WHERE feature_id = ? AND id = ?", dict["title"], dict["summary"], dict["severity"], dict["state"], feature_id, bug_id)

    return redirect("/feature/" + str(feature_id))



@app.route("/deletebug/<int:feature_id>/<int:bug_id>", methods=["GET"])
@login_required
def deletebug(feature_id, bug_id):
    """Deletes a Project in the projects table"""

    # Delete from the projects table
    db.execute("DELETE FROM bugs WHERE id = ?", bug_id)

    return redirect("/feature/" + str(feature_id))
