import os

import signal

from flask import Flask, request

from db_connector import user_connector

from flask import jsonify

import datetime

app = Flask(__name__)
   


@app.route('/api/users/userData/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    """An Route function that manages the API calls according to the request method

    Args:
        user_id ([int]): [The User ID from the API parameter]

    Returns:
        [json]: [Created user  
        /Updated user details
        /Deleted user
        /Returned user details with status code]
    """
    if request.method == 'POST':
        request_data = request.json
        user_name = request_data.get('user_name')
        try:
            user_connector.add_user(user_id, user_name)
            # status code
            return {'user id': user_id, 'user name': user_name, 'created at': datetime.datetime.now(), 'status': 'saved'}, 201
        except Exception as error:
            return jsonify(f"message:{error}"), 500

    if request.method == 'GET':
        try:
            value = user_connector.GetUserByID(user_id)
            if value == None:
                return jsonify("message: user not found"), 404
            return jsonify(value), 200
        except Exception as error:
            return jsonify(f"message:{error}"), 500

    if request.method == 'PUT':
        request_data = request.json
        user_name = request_data.get('user_name')
        try:
            user_connector.UpdateUser(user_id, user_name)
            if user_name == None:
                return {"user is not found"}, 404
            # status code
            return {'user id': user_id, 'user name': user_name, 'status': 'Updated'}, 200
        except Exception as error:
            return jsonify(f"message:{error}"), 500

    if request.method == 'DELETE':
        try:
            user_connector.DeleteUser(user_id)
            return jsonify(f"message: a user with the user id {user_id} has been succesfully deleted"), 200
        except Exception as error:
            return jsonify(f"message:{error}"), 500


app.run(host='127.0.0.1', debug=True, port=5000)
