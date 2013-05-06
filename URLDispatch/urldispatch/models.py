"""Models for our PyramidPress demo.

Instead of being 'complicated' and using persistence, instaces of these classes
are created at run-time for simple demonstration purposes. - see __init__

"""


class User:
    """Single user in our blogging system"""

    def __init__(self, username=None, name=None):
        # Users have usernames
        self.username = username
        # And they can publish pages on our system called pages.
        self.pages = {}

    def __repr__(self):
        """Better interactive prompt inspection for live demo"""
        return u'<User username="%s">' % self.username


class Page:
    """A page created by a user"""

    def __init__(self, user, title=None, content=None):
        """SubPages must be created with an owning user."""
        # Record user as owner of this page
        self.user = user
        # Save title and content if they were passed...
        self.title = title
        self.content = content
        # Stash this page in the user's account
        self.user.pages[title.lower()] = self

    def __repr__(self):
        """Better interactive prompt inspection for live demo"""
        params = (self.title, self.user.username)
        return u'<SubPage title="%s" owner="%s">' % params
