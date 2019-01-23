from api.search import Search
from createapp import create_app, db
from flask_restful import Api

# Create the app.
app = create_app()
# Push an application context to bind the SQLAlchemy object to your
# application.
app.app_context().push()

# Create app components.
api = Api(app)

# Add API endpoints.
api.add_resource(
    Search,
    '/api/search/<string:param>',
    '/api/search/<string:param>/rescrap',
)
