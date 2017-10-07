# from flask import Flask

# app = Flask(__name__)
# from app import views


from flask import Flask

app = Flask(__name__)

from api.routes import api

app.register_blueprint(api)
