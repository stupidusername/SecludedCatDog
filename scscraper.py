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

    :const str SEARCH_URL: identity search URL.
    """

    SEARCH_URL 'https://socialcatfish.com/search.html'

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
            params = {
                'email': param,
                'search_type': 1
            }
        else:
            # The search param is a phone number.
            params = {
                'phone': param,
                'phone': 3
            }
        # The country code of the search parameters appears to be always the
        # same one.
        params['country'] = 'US'
