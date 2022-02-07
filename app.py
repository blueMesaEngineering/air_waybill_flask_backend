from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from database.db import initialize_db
from resources.routes import initialize_routes
from flask_restful import Api
import logging

app = Flask(__name__)

logger = logging.getLogger('werkzeug') 
handler = logging.FileHandler('test.log') 
logger.addHandler(handler)

cors = CORS(app)
app.config.from_envvar('ENV_FILE_LOCATION')
app.config['PROPAGATE_EXCEPTIONS']  # https://stackoverflow.com/questions/54648603/how-should-i-handle-exceptions-raised-in-jwt-required-decorator-in-flask-jwt
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
  'host': 'mongodb://localhost/air_waybill_flask_backend'
}

initialize_db(app)
initialize_routes(api)

app.run()