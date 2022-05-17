import json
import os
import flask
from flask import request, jsonify, abort


CWD = os.getcwd()
MOCK_DATA_FOLDER = '/app/users/mock_data'

users_blueprint = flask.Blueprint('users', __name__, url_prefix='/app/users')


@users_blueprint.route('/', methods=['GET'])
def get_users():
    
    with open(f'{CWD}{MOCK_DATA_FOLDER}/users.json') as f:
        data = json.load(f)

    return jsonify(data)


@users_blueprint.route('/<int:pk>', methods=['GET'])
def get_user(pk):

    with open(f'{CWD}{MOCK_DATA_FOLDER}/users.json') as f:
        data = json.load(f)

        new_data = None

        for el in data:
            if int(el['id']) == pk:
                new_data = el
                return jsonify(new_data)

        if not new_data:
            abort(404)


@users_blueprint.route('/', methods=['POST'])
def post_user():
    content_type = request.headers.get('Content-Type')

    if (content_type == 'application/json'):
        post_data = request.get_json()

        with open(f'{CWD}{MOCK_DATA_FOLDER}/users.json', 'r+') as f:
            data = json.load(f)

            for el in range(len(data)):
                new_id = data[-1]['id'] + 1
               
                if data[el]['id'] != new_id:
                    pass
                else:
                    new_id += 1
                
            post_data['id'] = new_id
            data.append(post_data)
        
        with open(f'{CWD}{MOCK_DATA_FOLDER}/users.json', 'w') as f:
            json.dump(data, f)

    else:
        return 'Content-Type not supported!'

    return jsonify(data)


@users_blueprint.route('/<int:pk>', methods=['PATCH'])
def patch_user(pk):

    content_type = request.headers.get('Content-Type')

    with open(f'{CWD}{MOCK_DATA_FOLDER}/users.json', 'r+') as f:
        data = json.load(f)

        new_data = None

        for el in range(len(data)):
            if int(data[el]['id']) == pk:

                new_data = data[el]

                if (content_type == 'application/json'):
                    post_data = request.get_json()

                    for key, value in post_data.items():
                        if key in data[el]:
                            new_data[key] = value
                        else:
                            abort(400)

                    data[el] = new_data

                else:
                    return 'Content-Type not supported!'

        if not new_data:
            abort(404)
        else:
            with open(f'{CWD}{MOCK_DATA_FOLDER}/users.json', 'w') as f:
                json.dump(data, f)


    return jsonify(data)

    
