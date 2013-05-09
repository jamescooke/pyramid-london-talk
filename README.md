Pyramid Router Talk - Examples
==============================

This code was demonstrated at the first Pyramid London meetup [(meetup page)](http://www.meetup.com/The-London-Pyramid-Group/events/114457692/).

Slides are available on my [blog post](http://jamescooke.info/pyramid-london-talk-pyramid-router.html).

The demo code builds a very simple WordPress-like site called PyramidPress. It uses a fake database that you'll see in the `__init__` file. There are simple URLs for `/users` and `/user/page` to show a user's profile and page respectively.

The master branch includes a demonstration of 'URL Dispatch', the traversal branch changes this up into a traversal strategy.


Installing
----------

Build your `virtualenv` - this repository assumes it will be in the `env` folder and gitignores it.

    virtualenv --python=[ROUTE TO YOUR PYTHON]/bin/python env

Activate and `pip install` the requirements.

    source env/bin/activate
    pip install -r requirements.txt

Prepare the source for development.

    python setup.py develop

This will update the egg info and pull in packages.

Run the server with reload which is helpful.

    pserve development.ini --reload

And visit your local host. http://localhost:6543/ to see the URL dispatch in operation.

In order to experiment with traversal, checkout the traversal branch:

    git checkout traversal

And `pserve` should reload with the updated code.
