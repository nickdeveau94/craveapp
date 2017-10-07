from flask import Blueprint
from flask_restful import Api



# Register the flask_restufl API on the api Flask Blueprint
# All Resources inherit from the url_prefix declared on the Blueprint
api = Blueprint('api', __name__, url_prefix='/api')
API = Api(api)