from createapp import sc_scraper
from flask import request
from flask_restful import Resource


class Search(Resource):
    """
    Flask-RESTful resource.
    """

    def get(self, param: str) -> dict:
        """
        Get information from a vote pool.

        :param str id: Email or phone number of the entity to be searched.
        :returns: A dictionary with the information of an entity.
        """
        # If the URL used to access this endpoint ends with `/rescrap` the
        # identity information will be searched in Social Catfish instead of
        # doing it in the app DB.
        rescrap = request.path.endswith('/rescrap')
        return sc_scraper.search(param)
