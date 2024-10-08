#!/usr/bin/env python3
"""
Module to launch the flask application
"""
from flask import Flask, render_template
from typing import Any


# Declare flask application
app: Flask = Flask(__name__, template_folder="./templates")


@app.route("/")
def home() -> Any:
    """
    Home page route

    Returns:
        HTML: `0-index.html` in the `./templates` directory
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
