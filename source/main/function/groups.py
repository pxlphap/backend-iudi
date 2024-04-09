from source import db
from flask import request, make_response, jsonify
from sqlalchemy import or_, and_
from source.main.model.groups import Groups
from source.main.model.forumPosts import ForumPosts
from source.main.function.forum import viewPost, deletePost
from sqlalchemy import func
from datetime import datetime
from sqlalchemy.sql import label, text


def singleGroup(GroupID):
    try:
        chat = db.session.execute(text('Select * from `Groups` join `ForumPosts` on Groups.GroupID = ForumPosts.GroupID'))
        data = []
        for row in chat:
            post_data = viewPost(row[4])  
            data.append(post_data)
        
        group_name = row[2]

        return {'state': 200, 'GroupID': GroupID, 'GroupName': group_name, 'data': data}
    except Exception as e:
        print(e)
        return make_response(jsonify({'Status': 400, 'message': 'An error occurred!'}))


def allGroup():
    try:
        chat = db.session.execute(text('Select * from `Groups`'))
        data=[]
        for row in chat:
            group = {}
            group["GroupID"] = row.GroupID
            group["UserID"] = row.UserID
            group["GroupName"] = row.GroupName
            group["CreateAt"] = row.CreateAt
            data.append(group)
        return {'state': 200, 'data': data} 
    except Exception as e:
        print(e)
        return make_response(jsonify({'Status':400, 'message':'An error occurred!'}))
    
def updateGroup(GroupID):
    try:
        json_data = request.json
        group = Groups.query.get(GroupID)
        group.GroupName = json_data['GroupName']
        db.session.commit()
        return make_response(jsonify({'Status':200,'message':'Update group successfully!'}))
    except Exception as e:
        print(e)
        return make_response(jsonify({'Status':500,'message':'An error occurred!'}))

def countGroup():
    try:
        count = db.session.query(Groups).count()
        return make_response(jsonify({'Status':200, 'Count':count}))
    except Exception as e:
        return make_response(jsonify({'Status':500,'message':'An Error Occurred!'}))

def searchPostInGroup(GroupID, key):
    try:
        posts = (
            db.session.query(ForumPosts, Groups)
            .join(Groups, ForumPosts.GroupID == Groups.GroupID)
            .filter(
                Groups.GroupID == GroupID,
                or_(ForumPosts.Title.ilike(f"%{key}%"), ForumPosts.Content.ilike(f"%{key}%"))
            )
            .order_by(ForumPosts.PostTime.desc())
            .all()
        )

        if posts:
            posts_data = [
                {
                    'PostID': post.ForumPosts.PostID,
                    'UserID': post.ForumPosts.PostID,
                    'GroupID': post.ForumPosts.GroupID,
                    'Title': post.ForumPosts.Title,
                    'Content': post.ForumPosts.Content,
                    'PostTime': post.ForumPosts.PostTime,
                    'IPPosted': post.ForumPosts.IPPosted,
                    'PostLatitude': post.ForumPosts.PostLatitude,
                    'PostLongitude': post.ForumPosts.PostLongitude,
                    'GroupName': post.Groups.GroupName,
                    'CreateAt': post.Groups.CreateAt
                }
                for post in posts
            ]
            return jsonify({'status': 200, 'Posts': posts_data})
        else:
            return make_response(jsonify({'status': 404, 'Message': 'No posts found for the given key in the specified group'}), 404)

    except Exception as e:
        return make_response(jsonify({'status': 500, 'message': 'An error occurred while searching for posts'}), 500)


def addGroup(id):
    try:
        json_data = request.json
        group = Groups(UserID=id, GroupName=json_data['GroupName'])
        db.session.add(group)
        db.session.commit()
        
        return make_response(jsonify({'status': 200, 'message': 'Add Group Successfully!'}), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({'status': 400, 'message': 'An error occurred'}), 400)
        
def removeGroup(GroupID):
    try:
        group_need_delete= Groups.query.filter(Groups.GroupID == GroupID).first()

        if group_need_delete:
            post_to_delete = ForumPosts.query.filter_by(GroupID=GroupID).all()
            
            if post_to_delete:
                for post in post_to_delete:
                    post_id = post.PostID
                    deletePost(post_id)
                
            db.session.delete(group_need_delete)
            db.session.commit()
            return make_response(jsonify({'Status': 404, 'Message': 'The group deleted!'}), 404)
        else:
            return make_response(jsonify({'Status': 404, 'Message': 'The group not found!'}), 404)

    except Exception as e:
        return make_response(jsonify({'status': 500, 'message': 'An error occurred while deleting the post'}), 500)