from source import db
from flask import request, make_response, jsonify
from sqlalchemy import or_, and_
from source.main.model.forumPosts import ForumPosts
from source.main.model.forumPhotos import ForumPhotos
from source.main.model.favorite import Favorite
from source.main.function.postComments import *
from datetime import datetime
from sqlalchemy.sql import label, text

def addNewPost(id):
    try:
        if not request.json:
            return make_response(jsonify({'status': 400, 'message': 'Bad Request - No JSON data provided'}), 400)

        json_data = request.json

        required_fields = ['GroupID', 'Title', 'Content', 'PostLatitude', 'PostLongitude']
        for field in required_fields:
            if field not in json_data:
                return make_response(jsonify({'status': 400, 'message': f'Missing required field: {field}'}), 400)

        post = ForumPosts(
            UserID=id,
            GroupID=json_data['GroupID'],
            Title=json_data['Title'],
            Content=json_data['Content'],
            PostTime=datetime.now(),
            IPPosted=request.remote_addr,
            PostLatitude=json_data['PostLatitude'],
            PostLongitude=json_data['PostLongitude'])
        db.session.add(post)
        db.session.commit()

        # Add associated images (PhotoURL) if provided
        if 'PhotoURL' in json_data and isinstance(json_data['PhotoURL'], list):
            for url in json_data['PhotoURL']:
                image_post = ForumPhotos(PostID=post.PostID, PhotoURL=url, UploadTime=datetime.now())
                db.session.add(image_post)

        db.session.commit()
        
        # Retrieve and return the newly created post
        post_id = post.PostID
        return viewPost(post_id)

    except Exception as e:
        print(f"Error: {e}")
        return make_response(jsonify({'status': 500, 'message': 'An error occurred while creating the post'}), 500)


def viewPost(id):
    try:
        data = []
        post = ForumPosts.query.get(id)
        post_favorite_count = Favorite.query.filter(and_(Favorite.PostID == id, Favorite.FavoriteType == 1)).count()

        if post:
            post_data = {
                'UserID': post.UserID,
                'GroupID': post.GroupID,
                'Content': post.Content,
                'Title': post.Title,
                'PostTime': post.PostTime,
                'IPPosted': post.IPPosted,
                'PostLatitude': post.PostLatitude,
                'PostLongitude': post.PostLongitude,
                'FavoriteNumber': post_favorite_count
            }

            data.append(post_data)

            images = ForumPhotos.query.filter(ForumPhotos.PostID == post.PostID).all()
            photo_urls = [image.PhotoURL for image in images]

            if photo_urls:
                post_data['PhotoURL'] = photo_urls

            return {'status': 200, 'Post': data}
        else:
            return {'status': 404, 'message': 'Post not found'}

    except Exception as e:
        print(f"Error: {e}")
        return {'status': 500, 'message': 'An error occurred while viewing the post'}
    
def updatePost(PostID):
    try:
        data_json = request.json
        post_need_update = ForumPosts.query.filter(ForumPosts.PostID == PostID).first()
        
        if post_need_update:
            if 'Title' in data_json:
                post_need_update.Title = data_json['Title']
            if 'Content' in data_json:
                post_need_update.Content = data_json['Content']
            
            db.session.commit()
            return viewPost(PostID)
        else:
            return make_response(jsonify({'Status': 404, 'Message': 'The post not found!'}), 404)

    except Exception as e:
        return make_response(jsonify({'status': 500, 'message': 'An error occurred while updating the post'}), 500)


def deletePost(PostID):
    try:
        post_need_delete= ForumPosts.query.filter(ForumPosts.PostID == PostID).first()

        if post_need_delete:
            removeFavorite(PostID)
            removeAllComment(PostID)
            db.session.delete(post_need_delete)
            db.session.commit()
            return viewPost(PostID)
        else:
            return make_response(jsonify({'Status': 404, 'Message': 'The post not found!'}), 404)

    except Exception as e:
        return make_response(jsonify({'status': 500, 'message': 'An error occurred while deleting the post'}), 500)
    

def searchPost(key):
    try:
        posts = (
            ForumPosts.query
            .filter(or_(ForumPosts.Title.ilike(f"%{key}%"), ForumPosts.Content.ilike(f"%{key}%")))
            .order_by(ForumPosts.PostTime.desc())
            .all()
        )

        if posts:
            posts_data = [
                {'PostID': post.PostID,
                'UserID': post.PostID,
                'GroupID':post.GroupID ,
                'Title': post.Title,
                'Content': post.Content,
                'PostTime': post.PostTime,
                'IPPosted': post.IPPosted,
                'PostLatitude': post.PostLatitude,
                'PostLongitude': post.PostLongitude,
                }
                for post in posts
            ]
            return jsonify({'status': 200, 'Posts': posts_data})
        else:
            return make_response(jsonify({'status': 404, 'Message': 'No posts found for the given key'}), 404)

    except Exception as e:
        return make_response(jsonify({'status': 500, 'message': 'An error occurred while searching for posts'}), 500)
    
def favoritePost(UserID, PostID):
    try:
        post_favorite = Favorite.query.filter(and_(Favorite.UserID == UserID, Favorite.PostID == PostID)).first()

        if post_favorite:
            post_favorite.FavoriteType = not post_favorite.FavoriteType
        else:
            new_favorite = Favorite(UserID=UserID, PostID=PostID, FavoriteType=True, FavoriteTime=datetime.now())
            db.session.add(new_favorite)

        db.session.commit()
        return viewPost(PostID)

    except Exception as e:
        return make_response(jsonify({'status': 500, 'message': 'An error occurred while favoriting the post'}), 500)


def removeFavorite(PostID):
    try:
        post = ForumPosts.query.filter_by(PostID=PostID).first()
        
        if post:
            favorite_to_delete = Favorite.query.filter_by(PostID=PostID).all()
            
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

def getListPost(GroupID, PostFrom, PostTo):
    pass