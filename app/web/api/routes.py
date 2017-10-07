from flask import Blueprint
from flask_restful import Api

from geo.views import TestView, CoordinatesView, Sensor



# Register the flask_restufl API on the api Flask Blueprint
# All Resources inherit from the url_prefix declared on the Blueprint
api = Blueprint('api', __name__, url_prefix='/api')
API = Api(api)

API.add_resource(TestView, '/test/')
API.add_resource(CoordinatesView, '/coordinates/')
API.add_resource(Sensor, '/sensor/')
