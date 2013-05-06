from pyramid.config import Configurator

from models import User, Page


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""
    config = Configurator(settings=settings)

    # Route for home
    config.add_route('home', '/')

    # Route for user profiles
    config.add_route('profile', '/{username}')

    # Route for users' pages
    config.add_route('page', '/{username}/{page_title}')

    config.scan()
    return config.make_wsgi_app()


def make_fake_db():
    """Return a dictionary which is our emulated database."""
    data = {
        'users': {},
    }

    for name in ['eileen', 'bob', 'james', 'shinead']:
        data['users'][name] = User(username=name)

    # Eileen has no pages

    # Bob has one:
    Page(data['users']['bob'], title='Motors',
            content='I like motorbikes. Lots and lots.')

    # James has two:
    Page(data['users']['james'], title='Pyramid',
         content='Pyramid is a framework for building webapps.')
    Page(data['users']['james'], title='Python',
         content='Python is my favourite language.')

    # Shinead has three:
    Page(data['users']['shinead'], title='Chickens',
         content='Chickens lay eggs if you look after them.')
    Page(data['users']['shinead'], title='Hamsters',
         content='Hamsters can make fun pets, but keep them warm.')
    Page(data['users']['shinead'], title='Python',
         content='Python is a snake and I do not like it.')

    return data
