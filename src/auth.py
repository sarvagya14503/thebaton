from flask import Flask, render_template, Blueprint, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
from marshmallow import fields, Schema


auth = Blueprint('auth', __name__)

@app.route('/')
def index():
    return jsonify({'message': 'lol xd'})

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(public_id = str(uuid.uuid4()), first_name = data['first_name'], last_name = data['last_name'], username = data['username'], password = hashed_password, email = data['email'], email_verified = False, is_staff = False, is_admin = False, created_at = datetime.datetime.utcnow(), modified_at=datetime.datetime.utcnow())
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message' :'New user created!', 'success' : 'True'})


