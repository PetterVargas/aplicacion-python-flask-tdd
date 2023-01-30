from pathlib import Path

from flask import Flask, render_template


# Creación e inicialización de la app Flask
app = Flask(__name__)


@app.route("/")
def index():
    """Rederiza el index."""
    return render_template("index.html")
