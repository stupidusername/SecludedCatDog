from config import Config
from lxml import html
import re
from requests import Response, Session
from typing import Optional


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

    # Social Catfish URLs
    SEARCH_URL = 'https://socialcatfish.com/search.html'
    LOGIN_URL = 'https://socialcatfish.com/login.html'
    # Create request headers.
    HEADERS = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest'
    }

    def __init__(self):
        self._session = Session()

    def search(self, param: str) -> Optional[dict]:
        """
        Search an identity information by its email or phone number.

        :param str param: The email or phone number of the identity.
        :returns: A dictionary containing the identity information or `None` if
            the identity was not found.
        """
        if '@' in param:
            # The search param is an email.
            data = {
                'email': param,
                'search_type': 1
            }
        else:
            # The search param is a phone number.
            data = {
                'phone': param,
                'search_type': 3
            }
        # The country code of the search parameters appears to be always the
        # same one.
        data['country'] = 'US'
        # Send the request.
        r = self._session.post(
            self.SEARCH_URL,
            data=data,
            headers=self.HEADERS
        )
        # Get URL value from the response object.
        r_url = self._get_response_url(r)
        # Use the URL value to determine if we need to login, the identity was
        # not found or if the identity was found and returned.
        if '/search/' in r_url:
            # Response differs based on the type of the search.
            if '@' in param:
                # Identity not found.
                return None
            elif r_url.endswith('-0/'):
                # Identity not found.
                return None
        elif '/search-data.html' in r_url:
            # We need to login.
            self._login()
            # Send the request again with the logged in session.
            r = self._session.post(
                self.SEARCH_URL,
                data=data,
                headers=self.HEADERS
            )
            # Get the new URL value.
            r_url = self._get_response_url(r)
        # Check if we have the identity information.
        # Response differs based on the type of the search.
        if '@' in param:
            if '/person/' not in r_url:
                raise SCScraperException('Identity information not found.')
        elif not re.search(r'-([1-9]|\d\d+)/$', r_url):
            raise SCScraperException('Identity information not found.')
        return ':D'

    def _get_response_url(self, r: Response) -> str:
        """
        Get the URL value from the JSON response of the search request.

        :param Response r: Response of the search request.
        :returns: The URL value.
        """
        try:
            return r.json()['url']
        except ValueError:
            raise SCScraperException('Failed to decode JSON response.')
        except KeyError:
            raise SCScraperException('URL value not found.')

    def _login(self):
        """
        Use the credentials stored in the app config to login into Social
        Catfish.
        """
        # Send the login request.
        config = Config()
        data = {
            'action': 'login',
            'email': config.get_sc_username(),
            'password': config.get_sc_password()
        }
        r = self._session.post(self.LOGIN_URL, data=data, headers=self.HEADERS)
        # Check that the response object contains a status value.
        try:
            status = r.json()['status']
        except ValueError:
            raise SCScraperException('Failed to decode JSON response.')
        except KeyError:
            raise SCScraperException('Status value not found.')
        # Raise an exception if the login was not successful.
        if not status:
            raise SCScraperException(
                'The login into Social Catfish was not sucessful. Check the '
                'access credentials in the app configuration.'
            )
