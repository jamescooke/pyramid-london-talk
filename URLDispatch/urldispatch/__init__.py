from pyramid.config import Configurator

from models import User, Page


class Root(dict):
    """Root factory for our traversal demo."""
    def __init__(self, request):
        pass

    def __getitem__(self, username):
        """Allow Root to lookup users underneath it."""
        # SQLAlchemy:
        # user = Session.query(User).filter(User.username=username).first()

        # Simulation:
        user = make_fake_db()['users'][username]

        return user


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""
    config = Configurator(settings=settings, root_factory=Root)
    config.add_static_view('static', 'static', cache_max_age=3600)

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
