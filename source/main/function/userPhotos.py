from flask import jsonify, request, make_response
from source import db
from source.main.model.userPhotos import UserPhotos
from source.main.function.users import *
from flask_mail import *
from datetime import datetime

def addImage(id):
    try: 
        photo_url = request.json.get('PhotoURL')
        set_as_avatar = request.json.get('SetAsAvatar') 

        image_data = UserPhotos(
            PhotoURL=photo_url,
            UserID=id,
            UploadTime=datetime.now(),
            SetAsAvatar=set_as_avatar
        )
        if set_as_avatar == True:
            UserPhotos.query.filter(UserPhotos.UserID == id).update({"SetAsAvatar": 0})

        db.session.add(image_data)
        db.session.commit()
        
        return viewProfile(id)
                
    except Exception as e:
        print(e)
        return make_response(jsonify({'status': 500, 'message': 'An error occurred'}), 500)


def setAvatarFromProfile(id):
    try:
        json_data = request.json
        UserPhotos.query.filter(UserPhotos.UserID == id).update({"SetAsAvatar": 0})
        UserPhotos.query.filter(UserPhotos.PhotoID == json_data['PhotoID']).update({"SetAsAvatar":1})
        db.session.commit() 
        return{
            'PhotoID': json_data['PhotoID'],
            'UserID': id,
            'SetAsAvatar': True
        }
    except Exception as e:
        print(e)
        return make_response(jsonify({'status': 500, 'message':'An error occurred'}), 500)
    
def viewAllImage(id):
    try:
        data = []
        user_images = UserPhotos.query.filter(UserID=id).all()
        
        if user_images:
            for image_data in user_images:
                image_info = {
                    'PhotoID': image_data.PhotoID,
                    'PhotoURL': image_data.PhotoURL,
                    'UploadTime': image_data.UploadTime,
                    'SetAsAvatar': image_data.SetAsAvatar
                }
                data.append(image_info)
            return {'status': 200, 'UserID': id, 'Photos': data}
        else:
            return make_response(jsonify({'status': 404, 'message': 'User not found'}), 404)
    except Exception as e:
        print(e)
        return make_response(jsonify({'status': 500, 'message': 'An error occurred'}), 500)

def viewSingleImage(id):
    try:
        image_to_view = UserPhotos.query.get(id)

        if image_to_view:
            return {'PhotoID': image_to_view.PhotoID, 'PhotoURL': image_to_view.PhotoURL, 'UploadTime': image_to_view.UploadTime, 'SetAsAvatar': image_to_view.SetAsAvatar}
        else:
            return make_response(jsonify({'status': 404, 'message': 'Image not found'}), 404)
    except Exception as e:
        print(e)
        return make_response(jsonify({'status': 500, 'message': 'An error occurred'}), 500)

def deleteImageUser(id):
    try:
        image_to_delete = UserPhotos.query.get(id)

        if image_to_delete:
            db.session.delete(image_to_delete)
            db.session.commit()
            return make_response(jsonify({'status': 200, 'message': 'Image deleted successfully'}), 200)
        else:
            return make_response(jsonify({'status': 404, 'message': 'Image not found'}), 404)
    except Exception as e:
        print(e)
        return make_response(jsonify({'status': 500, 'message': 'An error occurred'}), 500)
