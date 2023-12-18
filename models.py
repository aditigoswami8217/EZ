
from flask_mongoengine import MongoEngine

db = MongoEngine()

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    is_ops_user = db.BooleanField(default=False)  

class File(db.Document):
    filename = db.StringField(required=True, unique=True)
    file_type = db.StringField(required=True, choices=['pptx', 'docx', 'xlsx'])
    secure_url = db.StringField(required=True, unique=True)
    uploaded_by = db.ReferenceField(User)
