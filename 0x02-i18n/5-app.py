#!/usr/bin/env python3
"""
Module to launch the flask application
Task 2
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import Any, Dict, Union


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {
        "name": "Teletubby",
        "locale": None,
        "timezone": "Europe/London",
    },
}


def get_user() -> Union[Dict, None]:
    """Retrieves a user based on a user id."""
    login_id = request.args.get("login_as")
    if login_id:
        return users.get(int(login_id))
    return None


class Config:
    """Configuration class for the Flask application"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Declare flask application
app: Flask = Flask(__name__, template_folder="./templates")
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@app.before_request
def before_request() -> None:
    """Performs some routines before each request's resolution."""

    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.

    Returns:
        str: best match
    """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(
        app.config["LANGUAGES"]
    )


@app.route("/")
def home() -> Any:
    """
    Home page route

    Returns:
        HTML: `0-index.html` in the `./templates` directory
    """
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    return render_template(
        "5-index.html", home_title=home_title, home_header=home_header
    )


if __name__ == "__main__":
    app.run(debug=True)
