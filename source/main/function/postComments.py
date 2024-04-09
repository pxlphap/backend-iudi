from flask import jsonify, request, make_response
from source import db
from source.main.model.postComments import PostComments
from source.main.model.commentFavorite import CommentFavorite
from source.main.model.users import Users
from source.main.model.forumPosts import ForumPosts
from source.main.model.commentPhotos import CommentPhotos
from flask_mail import *
from datetime import datetime
from sqlalchemy.sql import and_

def getAllComment(PostID):
    try:
        data = []
        all_comment = (
            db.session.query(
                PostComments,
                CommentFavorite.FavoriteType.label('FavoriteType'),
                CommentPhotos.PhotoURL.label('PhotoURL')
            )
            .select_from(PostComments) 
            .outerjoin(CommentFavorite, and_(
                CommentFavorite.CommentID == PostComments.CommentID
            ))
            .outerjoin(CommentPhotos, CommentPhotos.CommentID == PostComments.CommentID)
            .filter(PostComments.PostID == PostID)
            .order_by(PostComments.CommentTime.desc())
            .all()
        )
        
        for comment, favorite_type, photo_url in all_comment:
            comment_info = {
                'PostID': comment.PostID,
                'UserID': comment.UserID,
                'Content': comment.Content,
                'CommentTime': comment.CommentTime,
                'CommentUpdateTime': comment.CommentUpdateTime,
                'FavoriteType': favorite_type,
                'PhotoURL': photo_url
            }
            data.append(comment_info)

        return {'status': 200, 'Comments': data}
    except Exception as e:
        print(e)
        return make_response(jsonify({'status': 400, 'message': 'An error occurred when getting all comments'}))

    
def addComment(UserID, PostID):
    try:
        json_data = request.json
        post = ForumPosts.query.filter(ForumPosts.PostID == PostID).first()
        user = Users.query.filter(Users.UserID == UserID).first()
        if post and user:
            comment = PostComments(PostID=PostID, UserID=UserID, Content=json_data['Content'],CommentTime=datetime.now(), CommentUpdateTime=datetime.now())
            db.session.add(comment)
            db.session.commit()
            
            if 'PhotoURL' in json_data and isinstance(json_data['PhotoURL'], list):
                for url in json_data['PhotoURL']:
                    image_comment = CommentPhotos(CommentID=comment.CommentID, PhotoURL=url, UploadTime=datetime.now())
                    db.session.add(image_comment)

            db.session.commit()
            
            return make_response(jsonify({'Status': 200, 'message': 'Add comment successfully!'}))
        else:
            return make_response(jsonify({'Status': 400, 'message': 'Post not found!'}))
    except Exception as e:
        return make_response(jsonify({'Status':500,'message':'An error occurred when get add comment!'}))
    
    
def favoriteComment(UserID, CommentID):
    try:
        comment_favorite = CommentFavorite.query.filter(and_(CommentFavorite.UserID == UserID, CommentFavorite.CommentID == CommentID)).first()

        if comment_favorite:
            comment_favorite.FavoriteType = not comment_favorite.FavoriteType
            db.session.commit()
            return make_response(jsonify({'status': 200, 'message':'Sucessfully!'}))
        else:
            new_favorite = CommentFavorite(UserID=UserID, CommentID=CommentID, FavoriteType=True, FavoriteTime=datetime.now())
            db.session.add(new_favorite)
            db.session.commit()
            return make_response(jsonify({'status': 200, 'message':'Favorite Sucessfully!'}))

    except Exception as e:
        print(e)
        return make_response(jsonify({'status': 500, 'message': 'An error occurred while favoriting the post'}), 500)
    
    
def removeImageComment(CommentID):
    try:
        comment = PostComments.query.filter_by(CommentID=CommentID).first()
        
        if comment:
            images_to_delete = CommentPhotos.query.filter_by(CommentID=CommentID).all()
            
            if images_to_delete:
                for image in images_to_delete:
                    db.session.delete(image)
                db.session.commit()
                
                return make_response(jsonify({'status': 200, 'message': 'All images deleted successfully'}), 200)
            else:
                return make_response(jsonify({'status': 404, 'message': 'No images found for the comment'}), 404)
        else:
            return make_response(jsonify({'status': 404, 'message': 'Comment not found'}), 404)
    except Exception as e:
        print(e)
        return make_response(jsonify({'status': 500, 'message': 'An error occurred while deleting images'}), 500)


def removeFavoriteComment(CommentID):
    try:
        comment = PostComments.query.filter_by(CommentID=CommentID).first()
        
        if comment:
            favorite_to_delete = CommentFavorite.query.filter_by(CommentID=CommentID).all()
            
            if favorite_to_delete:
                for favorite in favorite_to_delete:
                    db.session.delete(favorite)
                
                db.session.commit()
                
                return make_response(jsonify({'status': 200, 'message': 'All Favorite deleted successfully'}), 200)
            else:
                return make_response(jsonify({'status': 404, 'message': 'No Favorite found for the comment'}), 404)
        else:
            return make_response(jsonify({'status': 404, 'message': 'Comment not found'}), 404)
    except Exception as e:
        print(e)
        return make_response(jsonify({'status': 500, 'message': 'An error occurred while deleting images'}), 500)
    
def removeComment(CommentID):
    try:
        comment = PostComments.query.filter_by(CommentID=CommentID).first()
        
        if comment:
            removeFavoriteComment(CommentID)
            removeImageComment(CommentID)
            comment_to_delete = PostComments.query.filter_by(CommentID=CommentID).first()
            db.session.delete(comment_to_delete)
            db.session.commit()
                
            return make_response(jsonify({'status': 200, 'message': 'All Favorite deleted successfully'}), 200)
        else:
            return make_response(jsonify({'status': 404, 'message': 'Comment not found!'}), 404)
        
    except Exception as e:
        print(e)
        return make_response(jsonify({'status': 500, 'message': 'An error occurred while deleting images'}), 500)
    
def removeAllComment(PostID):
    try:
        post = ForumPosts.query.filter_by(PostID=PostID).first()
        
        if post:
            comment_to_delete = PostComments.query.filter_by(PostID=PostID).all()
            
            if comment_to_delete:
                for comment in comment_to_delete:
                    comment_id = comment.CommentID
                    removeComment(comment_id)
                
                return make_response(jsonify({'status': 200, 'message': 'All Comment deleted successfully'}), 200)
            else:
                return make_response(jsonify({'status': 404, 'message': 'No Comment found for the comment'}), 404)
        else:
            return make_response(jsonify({'status': 404, 'message': 'Comment not found'}), 404)
    except:
        return make_response(jsonify({'Status':500,'message':'An error occurred!'}))