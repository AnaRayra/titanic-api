from app.error_handler.error_handler import InvalidUsage
from flask import Flask, request
import app.service as service
from flask import jsonify
from app import app

@app.route('/')
def home():
    return "API Available!!!"

@app.route('/predict', methods=['POST'])
def create_task():
    request_data = request.get_json()
    return {"response": service.people_prediction(request_data)}

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
