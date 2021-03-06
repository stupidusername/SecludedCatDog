from configparser import ConfigParser
from pathlib import Path


class Config(object):
    """
    This class provides access to the app configuration.
    """

    def __init__(self):
        self._config = ConfigParser()
        self._config.read(Path('config.ini'))

    def get_secret_key(self) -> str:
        """
        :returns: Secret key for cookies.
        """
        return self._config['DEFAULT']['secret_key']

    def get_sql_alchemy_url(self) -> str:
        """
        :returns: Database DSN.
        """
        return self._config['DEFAULT']['sqlalchemy.url']

    def get_sc_username(self) -> str:
        """
        :returns: Social Catfish user.
        """
        return self._config['DEFAULT']['sc_username']

    def get_sc_password(self) -> str:
        """
        :returns: Social Catfish password.
        """
        return self._config['DEFAULT']['sc_password']
