from collections import namedtuple

User = namedtuple("User", "name role expired")
USER, ADMIN = "user", "admin"
SECRET = "I am a very secret token"

julian = User(name="Julian", role=USER, expired=False)
bob = User(name="Bob", role=USER, expired=True)
pybites = User(name="PyBites", role=ADMIN, expired=False)
USERS = (julian, bob, pybites)


class Error(Exception):
    """Base class for other exceptions"""

    pass


class UserDoesNotExist(Error):
    """Raised when user does not exist"""

    pass


class UserAccessExpired(Error):
    """Raised when user access has expired"""

    pass


class UserNoPermission(Error):
    """Raised when user does not have the right permission"""

    pass


def get_secret_token(username):
    usernames = [user.name for user in USERS]
    if username not in usernames:
        raise UserDoesNotExist
    else:
        person = [user for user in USERS if user.name == username][0]
        if person.expired:
            raise UserAccessExpired
        if person.role != ADMIN:
            raise UserNoPermission
    return SECRET

