# file.py

from flask import request
from flask_restful import Resource
from models import File, User

class FileUpload(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username') 
        user = User.objects(username=username).first()

        if user:
            if user.is_ops_user:  
                if data['file_type'] in ['pptx', 'docx', 'xlsx']:
                    new_file = File(filename=data['filename'], file_type=data['file_type'], secure_url=data['secure_url'], uploaded_by=user)
                    new_file.save()
                    return {'message': 'File uploaded successfully'}, 201
                else:
                    return {'message': 'Invalid file type. Only pptx, docx, and xlsx are allowed.'}, 400
            else:
                return {'message': 'Unauthorized. Only Ops User can upload files.'}, 403
        else:
            return {'message': 'User not found'}, 404

class FileDownload(Resource):
    def get(self, assignment_id):
        username = request.args.get('username') 
        user = User.objects(username=username).first()

        file = File.objects(id=assignment_id, uploaded_by=user).first()
        if file:
        
            secure_url = generate_secure_url(file)
            return {'download-link': secure_url, 'message': 'success'}, 200
        else:
            return {'message': 'File not found or unauthorized access'}, 404
