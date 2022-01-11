#!/bin/bash

export ENV_FILE_LOCATION=./.env
wait
echo "ENV_FILE_LOCATION: " $ENV_FILE_LOCATION
wait
pipenv install flask_jwt_extended flask_restful flask_mongoengine
wait
pipenv install && pipenv shell
wait
python app.py
