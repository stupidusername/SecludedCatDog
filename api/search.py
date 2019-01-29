from createapp import db, sc_scraper
from datetime import datetime
from flask import request
from flask_restful import Resource
from models.search import Search as SearchModel
from scscraper import SCScraperException


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
        search = None
        if not rescrap:
            search = \
                SearchModel.query.filter(SearchModel.param == param).first()
        if rescrap or not search:
            # Rescrap was specified or the record was not found in the app DB.
            # Get the identity information from Social Catfish.
            try:
                identity = sc_scraper.search(param)
                if identity:
                    # Save the identity in the app DB.
                    search = self._save_search(param, identity)
                else:
                    # The identity was not found.
                    response = {
                        'success': False,
                        'error': 'The indentity was not found.'
                    }
            except SCScraperException as e:
                # There was an error while getting the information.
                response = {
                    'success': False,
                    'error': str(e)
                }
        # If the search was completed build a successful response.
        if search:
            response = {
                'success': True,
                'create_datetime': \
                    search.create_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                'identity': search.identity
            }
        # Send request response.
        return response

    def _save_search(self, param: str, identity: dict) -> SearchModel:
        """
        Save the identity in the app DB.

        :param param str: Search param.
        :param dict identity: identity information.
        """
        # Check the DB to know if the record was already saved.
        search = SearchModel.query.filter(SearchModel.param == param).first()
        if not search:
            # Create a new record.
            search = SearchModel()
        # Save the information.
        search.param = param
        search.create_datetime = datetime.utcnow()
        search.identity = identity
        db.session.add(search)
        db.session.commit()
        # Return the search model.
        return search
