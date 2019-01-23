from config import Config
from lxml import html
from requests import Session


class SCScraperException(Exception):
    """
    An exception raised by a Social Catfish scraper.
    """
    pass


class SCScraper(object):
    """
    Social Catfish scraper.
    """

    def __init__(self):
        self._session = Session()

    def search(self, param: str) -> dict:
        """
        Search an identity information by its email or phone number.

        :param str param: The email or phone number of the identity.
        :returns: A dictionary containing the identity information.
        """
        if '@' in param:
            # The search param is an email.
            return 'email'
        else:
            # The search param is a phone number.
            return 'phone_number'
