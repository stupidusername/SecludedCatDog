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
        return param
