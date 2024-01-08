"""
helpers.py

These are the helper functions. Many will be heavily inspired by the Finance
Assignment. Source Citation will be included in the Specification of each
Function.


Author: Nick Foerster
Date: 12/23/23
"""

from flask import redirect, render_template, session, request
from functools import wraps


def escape(s):
    """
    Escape special characters.

    https://github.com/jacebrowning/memegen#special-characters
    """
    for old, new in [
        ("-", "--"),
        (" ", "-"),
        ("_", "__"),
        ("?", "~q"),
        ("%", "~p"),
        ("#", "~h"),
        ("/", "~s"),
        ('"', "''"),
    ]:
        s = s.replace(old, new)
    return s


def apology(message, code=400):
    """
    Render message as an apology to user.

    Provided by the Finance Assignment.
    """
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    Original Citation (Broken Link):
    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/

    Updated Citation:
    https://flask.palletsprojects.com/en/3.0.x/patterns/viewdecorators/

    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def query_val(query, key):
    """
    A simple function to return the output of a execute command as a string.
    Meant for queries whose purpose is to return a single value.

    Parameters:
    query   - A dictionary list
    key     - A string

    Example:
    value = query_val(db.execute("SELECT...", "key"))

    Meant to replace having to do this:
    u = db.execute("SELECT username FROM users WHERE id = ?", user_id)
    user = u[0]["username"]
    With this:
    user = query_val(db.execute(
        "SELECT username FROM users WHERE id = ?",
        user_id), "username")

    Returns a String
    """
    return query[0][key]


def uid_val():
    """
    A simple function to reformat the user id returned by session[].
    This is to fix a strange issue with session where the datatype for session's return value changes.

    Parameters: None

    Example:
    user_id = uid_val()

    Returns an Integer
    """

    # Create variable for the current logged in user using session[]
    uid = session["user_id"]

    # Here is a fix that will ensure no errors
    if type(uid) is list:
        user_id = uid[0]["id"]
    elif type(uid) is dict:
        user_id = uid["id"]
    elif type(uid) is int:
        user_id = uid
    else:
        return apology("UID datatype invalid. Please contact support!", 400)

    return int(user_id)


def get_form_submissions(number):
    """
    A function that retrieves values from the current page's form submissions,
    checks that they are not empty,
    then adds them to a Dictionary for ease of use.

    *** NOTE: I decided to leave Register and Login get.forms and validations as they were ***

    Parameters:
    number  - An Integer

    Example:
    dict = get_form_submissions(2)

    dict["title"]

    Returns a Dictionary
    """
    dict = {}

    if number == 2:
        # Get the submitted title for the page
        title = request.form.get("title")
        # Get the submitted summary for the page
        summary = request.form.get("summary")

        # Ensure title is not empty
        if not title or title == "":
            return apology("Could not retrieve title value!")
        # Ensure summary is not empty
        if not summary or summary == "":
            return apology("Could not retrieve summary value!")

        dict = {
            "title": title,
            "summary": summary
            }


    elif number == 4:
        # Get the submitted title for the page
        title = request.form.get("title")
        # Get the submitted summary for the page
        summary = request.form.get("summary")
        # Get the submitted severity for the page
        severity = request.form.get("severity")
        # Get the submitted state for the page
        state = request.form.get("state")

        # Ensure title is not empty
        if not title or title == "":
            return apology("Could not retrieve title value!")
        # Ensure summary is not empty
        if not summary or summary == "":
            return apology("Could not retrieve summary value")
        # Ensure severity is not empty
        if not severity or severity == "":
            return apology("Could not retrieve severity value!")
        # Ensure state is not empty
        if not state or state == "":
            return apology("Could not retrieve state value!")

        dict = {
            "title": title,
            "summary": summary,
            "severity": severity,
            "state": state
            }

    else:
        return apology("Incorrect number of form submissions. Please contact support!", 400)

    return dict
