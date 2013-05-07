Pyramid Router Talk - Examples
==============================

Installing
----------

Build your `virtualenv` - this repository assumes it will be in the `env` folder and gitignores it.

    virtualenv --python=[ROUTE TO YOUR PYTHON]/bin/python env

Activate and `pip install` the requirements.

    source env/bin/activate
    pip install -r requirements.txt

There is a separate project for each example code - URLDispatch & Traversal.

Prepare the source for development.

    python setup.py develop

This will update the egg info and pull in packages.

Run the server with reload which is helpful.

    pserve development.ini --reload

And visit your local host. http://localhost:6543/
