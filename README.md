# Restful API using Flask

Using Flask (a Python Web Framework) to build a basic REST API

SQL Alchemy - an Object Relational Mapper
it is an astraction layer that allows us to interact with the database without having to write SQL queries

Marshmallow -
we bring it in and pass it into our Schema - it serialises and deserialises our Objects

Create virtual environment using `pipenv`
It keeps all dependencies in one place similar to `npm` for Node.js

`python --version` Python 3.11.3

Python Package Manager `pip`

`pip install pipenv`

is used to install the Pipenv package manager tool.

Pipenv is a higher-level tool built on top of `pip` that combines package dependency management with virtual environment management.

When you run `pip install pipenv`, the following actions typically occur:

1. **Installation**: Pip, the default Python package installer, is used to download the latest version of the Pipenv package from the Python Package Index (PyPI).
2. **Dependency resolution**: Pip resolves any dependencies required by Pipenv and ensures they are installed.
3. **Installation of Pipenv**: Once the dependencies are resolved, Pip installs the Pipenv package on your system.
4. **Environment setup**: After installation, Pipenv creates a virtual environment for your project, if one doesn't already exist. A virtual environment provides an isolated Python environment specific to your project, keeping the dependencies separate from the system's Python installation and other projects.
5. **Configuration**: Pipenv sets up the project-specific configuration files, namely the `Pipfile` and `Pipfile.lock`. These files store information about the project's dependencies, including their versions and any constraints.
6. **Activation**: If the virtual environment was created, Pipenv automatically activates it, making it the active Python environment for your current shell session.

By using Pipenv, you can easily manage your project's dependencies, create reproducible development environments, and ensure consistent installations across different systems.

`pipenv shell`
This will activate your virtual environment and create a `Pipfile` which holds all of the dependencies/packages to you install.

The `pipenv shell` command is used to activate the virtual environment created by Pipenv for your project. When you run `pipenv shell`, the following actions typically occur:

1. **Environment activation**: Pipenv activates the virtual environment associated with your project. This means that any subsequent Python or pip commands will use the Python interpreter and packages installed within the virtual environment instead of the global system Python installation.
2. **Environment variables**: Pipenv sets up environment variables specific to the virtual environment, such as modifying the `PATH` variable to prioritize the virtual environment's `bin` directory. This ensures that when you run commands like `python` or `pip`, they refer to the versions installed within the virtual environment.
3. **Shell prompt change**: After activation, your shell prompt is updated to reflect that you are now working within the virtual environment. Typically, you will see the name of the virtual environment displayed in the prompt, indicating that you are in the activated state.

By activating the virtual environment using `pipenv shell`, you can work within an isolated Python environment specific to your project. This helps ensure that the dependencies and packages you install or modify do not interfere with other projects or the system's Python installation. It provides a clean and consistent environment for your project's development and execution.

Install `flask`, `flask-sqlalchemy`, `flask-marshmallow` and `marshmallow-sqlalchemy` (to help sqlalchemy and marshmallow to integrate):

`pip install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy`

```
$ pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy
Installing flask...
Resolving flask...
Installing...
Adding flask to Pipfile's [packages] ...
Installation Succeeded
Installing flask-sqlalchemy...
Resolving flask-sqlalchemy...
Installing...
Adding flask-sqlalchemy to Pipfile's [packages] ...
Installation Succeeded
Installing flask-marshmallow...
Resolving flask-marshmallow...
Installing...
Adding flask-marshmallow to Pipfile's [packages] ...
Installation Succeeded
Installing marshmallow-sqlalchemy...
Resolving marshmallow-sqlalchemy...
Installing...
Adding marshmallow-sqlalchemy to Pipfile's [packages] ...
Installation Succeeded
Pipfile.lock not found, creating...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
Success!
Locking [dev-packages] dependencies...
Updated Pipfile.lock (fe1f50775bddf0262d7c24d1dcc5e37d817b10c2348eebc4881fbc1e49aae5a4)!
Installing dependencies from Pipfile.lock (aae5a4)...
```

We create an `app.py` file:

And in it we add the import statements:

```
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
```

We then initialise the app:

```
app = Flask(__name__)
```

Before we run the server check if the `app.py` is the main file.

Then `app.run()` and pass it the option of `debug=True` since we are in development

```
if __name__ == "__main__":
    app.run(debug=True)
```

We can run the server now, in the command line:

`python app.py`

```
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```
