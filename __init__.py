# app/__init__.py

from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Use pymongo to connect to MongoDB using the provided URI
client = MongoClient(app.config['MONGODB_URI'], server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Set up Flask extensions (MongoEngine and CORS)
db = MongoEngine(app)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Import resources after initializing app and db
from app import models, auth, file

# Check MongoDB connection status
@app.route('/check_mongodb_connection', methods=['GET'])
def check_mongodb_connection():
    try:
        # Attempt to query the database
        db.connection.server_info()
        return {'status': 'success', 'message': 'MongoDB is connected'}, 200
    except Exception as e:
        return {'status': 'error', 'message': f'MongoDB connection error: {str(e)}'}, 500

# Define a root route
@app.route('/', methods=['GET'])
def hello_world():
    return {'message': 'Hello, World!'}
