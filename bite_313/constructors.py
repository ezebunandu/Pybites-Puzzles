import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:
    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        if not re.match(r".*\.[a-z]{2,3}$", name):
            raise DomainException
        self.name = name

    # next add a __str__ method and write 2 class methods
    def __str__(self):
        return f"{self.name}"

    @classmethod
    def parse_url(cls, url):
        d = re.findall(r"https?://([A-Za-z_0-9.-]+).*", url)[0]
        return cls(d)

    @classmethod
    def parse_email(cls, email):
        d = email.split("@")[1]
        return cls(d)
