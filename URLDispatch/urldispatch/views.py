from pyramid.view import view_config

from . import make_fake_db, Root
from .models import User, Page

"""Views below use the fake database, but SQLAlchemy example are included."""


@view_config(context=Root, renderer='home.mako')
def home_view(request):
    """Show PyramidPress home page with a list of users."""

    # SQLAlchemy:
    # users = Session.query(User).all()

    # Simulation:
    users = make_fake_db()['users'].itervalues()

    return {
        'users': users,
    }


@view_config(context=User, renderer='profile.mako')
def profile_view(request):
    """Show single user's profile with their pages."""

    user = request.context
    pages = user.pages.itervalues()

    return {
        'user': user,
        'pages': pages,
    }


@view_config(context=Page, renderer='page.mako')
def page_view(request):
    """Show a single page belonging to a user."""

    page = request.context
    user = page.user

    return {
        'user': user,
        'page': page,
    }
