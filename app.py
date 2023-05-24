# we first import flask and the methods we need
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# the core os module we can use to deal with file paths etc.
import os

# Initialise our app with Flask
app = Flask(__name__)

# Run the Server
# check to see if this is the main file
if __name__ == "__main__":
    # take the app object and pass run() and pass an option of debug=True (since we are in development)
    app.run(debug=True)
