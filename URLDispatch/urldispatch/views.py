from pyramid.view import view_config

from . import make_fake_db

"""Views below use the fake database, but SQLAlchemy example are included."""


@view_config(route_name='home', renderer='home.mako')
def home_view(request):
    """Show PyramidPress home page with a list of users."""

    # SQLAlchemy:
    # users = Session.query(User).all()

    # Simulation:
    users = make_fake_db()['users'].itervalues()

    return {
        'users': users,
    }


@view_config(route_name='profile', renderer='profile.mako')
def profile_view(request):
    """Show single user's profile with their pages."""

    # URLDispatch means that we need to load the target object...
    # username comes from matchdict...
    username = request.matchdict['username']

    # SQLAlchemy:
    # user = Session.query(User).filter(User.username=username).first()

    # Simulation:
    user = make_fake_db()['users'][username]
    pages = user.pages.itervalues()

    return {
        'user': user,
        'pages': pages,
    }


@view_config(route_name='page', renderer='page.mako')
def page_view(request):
    """Show a single page belonging to a user."""

    # Pull in the vars from the matchdict
    username = request.matchdict['username']
    page_title = request.matchdict['page_title']

    # Load the object from the matchdict

    # SQLAlchemy:
    # page = Session.query(Page).filter(Page.user.username==username).filter(Page.title

    user = make_fake_db()['users'][username]
    page = user.pages[page_title]

    return {
        'user': user,
        'page': page,
    }
