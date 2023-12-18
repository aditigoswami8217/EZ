# auth.py

from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash
from models import User

class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = User(username=data['username'], password=hashed_password, email=data['email'])
        new_user.save()
        return {'message': 'User created successfully'}, 201

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        user = User.objects(username=data['username']).first()
        if user and check_password_hash(user.password, data['password']):
            return {'message': 'Login successful'}, 200
        else:
            return {'message': 'Invalid credentials'}, 401
