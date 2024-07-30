#!/usr/bin/env python3
"""
Module to launch the flask application
Task 1
"""
from flask import Flask, render_template
from flask_babel import Babel
from typing import Any


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


@app.route("/")
def home() -> Any:
    """
    Home page route

    Returns:
        HTML: `0-index.html` in the `./templates` directory
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
