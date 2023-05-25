# we first import flask and the methods we need
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# the core os module we can use to deal with file paths etc.
import os

# Initialise our app with Flask
app = Flask(__name__)

# Setup our SQL Alchemy Base URI
# we set the basedir as the os . path . absolute path
# and os.path.dirname is the current folder we are in, and then the file we are in
basedir = os.path.abspath(os.path.dirname(__file__))

# Setup our Database
# locate the folder we are currently in and then the file that we will use for the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "db.sqlite"
)
# we don't need this but it will complain in the console,
# it is used to disable SQLAlchemy's modification tracking feature.
# in many cases, the modification tracking feature is not necessary or may introduce some overhead that is not needed for the application.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialise Marshmallow
ma = Marshmallow(app)

# Initialise the Database, by calling SQLAlchemy and pass in our app.
db = SQLAlchemy(app)


@app.route("/", methods=["GET"])
def get():
    return jsonify({"message": "Hello World"})


# We create a Product Class/Model
# it gets passed in db which is our SQLAlchemy, and then using the Model class, we have a bunch of predefined methods
class Product(db.Model):
    # the way to make a field is db.Column()
    # it takes in [1] data type,
    id = db.Column(db.Integer, primary_key=True)
    # we don't want 2 products to have the same name
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    # We need our Constructor, passing in "self" (similar to "this")
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# Product Schema
# this where we use Marshmallow
class ProductSchema(ma.Schema):
    # these are the fields that are allowed to show (if you didn't want to show the id)
    class Meta:
        fields = ("id", "name", "description", "price", "quantity")


# Initialise the Schema
product_schema = ProductSchema()
# When loading data into the ProductSchema, only the fields defined in the Meta class (("id", "name", "description", "price", "quantity")) will be considered and any other fields present in the input data will raise an error.

# depending on what we are doing, we are either dealing with many products (getting a list of many), or a single product (updating or getting a single product)
products_schema = ProductSchema(many=True)

# Run the Server
# check to see if this is the main file
if __name__ == "__main__":
    # take the app object and pass run() and pass an option of debug=True (since we are in development)
    app.run(debug=True)
