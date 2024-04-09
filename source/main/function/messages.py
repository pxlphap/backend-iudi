from source import db
from flask import request, make_response, jsonify

from source.main.model.messages import Messages
from source.main.model.relationships import Relationships
from sqlalchemy import func
from datetime import datetime
from sqlalchemy.sql import label, text


def messages(id):
    if (request.method=="GET"):
        try:
            chat = db.session.execute(text(
            'Select * from Users inner join messages on users.UserID= messages.UserID'))
            data=[]
            for row in chat:
                view_chat = {}
                view_chat["UserID"] = row.UserID
                view_chat["Username"] = row.Username
                view_chat["Email"] = row.Email
                view_chat["Phone"] = row.Phone
                view_chat["Password"] = row.Password
                view_chat["Gender"] = row.Gender
                view_chat["BirthDate"] = row.BirthDate
                view_chat["BirthTime"] = row.BirthTime
                view_chat["Avatar"] = row.Avatar
                view_chat["HometownLocationID"] = row.HometownLacationID
                view_chat["CurrentLocationID"] = row.CurrentLocationID
                view_chat["IPRegistration"] = row.IPRegistration
                view_chat["IPCurrent"] = row.IPCurrent
                view_chat["IsAnonymous"] = row.IsAnonymous
                view_chat["MessageID"] = row.MessageID
                view_chat['SenderID'] = row.SenderID
                view_chat["ReceiverID"] = row.ReceiverID
                view_chat['Context'] = row.Context
                view_chat['MessageTime'] = row.MessageTime
                view_chat['IsSeen'] = row.IsSeen
                data.append(view_chat)
            return {'state': 200, 'data': data} 
        except Exception as e:
            print(e)
            return make_response(jsonify({'status': 400, 'message': 'Request fail. Please try again'}), 400)
    if (request.method=="POST"):
            json = request.json         
            try:
                message_time = datetime.strptime( 
                    json['MessageTime'], '%d/%m/%Y %H:%M %p %z')
                newmessage=messages(sendAt=message_time,idReceive=id,text=json['content'])               
                if (json['idSend']):
                    newmessage.SenderID=json['SenderID']
                db.session.add(newmessage)
                db.session.commit()
                chat_parse = {}
                chat_parse["MessageID"] = newmessage.MessageID
                chat_parse['SenderID'] = newmessage.SenderID
                chat_parse["ReceiverID"] = newmessage.ReceiverID
                chat_parse['Context'] = newmessage.Context
                chat_parse['MessageTime'] = newmessage.MessageTime
                chat_parse['IsSeen'] = newmessage.IsSeen
                return {'status': 200, 'message': chat_parse}
            except:
                return make_response(jsonify({'status': 300, 'message': 'Request fail. Please try again'}), 300)
    if request.method=="DELETE":
        pass
def blockchat(id):
    if (request.method=="GET"):
        try:
            chat = db.session.execute(text(
            'Select * from Users inner join Relationships on Users.UserID=Relationships.BlockedUserID'))
            data=[]
            for row in chat:
                view_chat = {}
                view_chat["idSend"] = row.idSend
                view_chat["idReceive"] = row.idReceive
                view_chat["relationship"] = row.relation
                data.append(view_chat)
            return {'state': 200, 'data': data} 
        except Exception as e:
            print(e)
            return make_response(jsonify({'status': 400, 'message': 'Request fail. Please try again'}), 400)
    if (request.method=="POST"):
            json = request.json  # Get JSON data from the request
            try:
                # Try to find an existing relationship in the database based on certain conditions
                user1 = Relationships.query.filter(
                    (Relationships.idSend == id) & (Relationships.idReceive == json['idReceive'])).first()
                user2 = Relationships.query.filter(
                    (Relationships.idReceive == id) & (Relationships.idSend == json['idReceive'])).first()
                if user1 or user2:
                    # If a relationship exists, return its status
                    return {'status': 200, 'relation is': user1.relation}
                else:
                    # If no relationship exists, create a new one with relation set to True
                    new_relation1 = Relationships(idSend=id, idReceive=json['idReceive'], relation=True)
                    new_relation2 = Relationships(idReceive=id, idSend=json['idReceive'], relation=True)
                    db.session.add(new_relation1)
                    db.session.add(new_relation2)
                    db.session.commit()
                    
                    # Prepare a response message
                    chat_parse = {
                        "id": new_relation1.id,
                        "idSend": new_relation1.idSend,
                        "idReceive": new_relation1.idReceive,
                        "relation": new_relation1.relation
                    }
                    
                    # Return a JSON response with the newly created relationship data
                    return {'status': 200, 'message': chat_parse}
            except Exception as e:
                # Handle exceptions, e.g., database errors
                print(e)
                return make_response(jsonify({'status': 300, 'message': 'Request fail. Please try again'}), 300)
    if (request.method=="PATCH"):
            json = request.json  # Get JSON data from the request
            try:
                # Try to find an existing relationship in the database based on certain conditions
                user = Relationships.query.filter(
                    (Relationships.idSend == id) & (Relationships.idReceive == json['idReceive'])
                ).first()
                if user:
                    # If a relationship exists, return its status
                    user.relation = json["relation"]
                    db.session.commit()
                    chat_parse = {
                        "id": user.id,
                        "idSend": user.idSend,
                        "idReceive": user.idReceive,
                        "relation": user.relation
                    }
                    return {'status': 200, 'message': chat_parse}
                else:
                    return {'status': 200, 'message':"no relationship"}
            except Exception as e:
                # Handle exceptions, e.g., database errors
                print(e)
                return make_response(jsonify({'status': 300, 'message': 'Request fail. Please try again'}), 300)
def statemessage(id):
    try:
        if(request.method=="POST"):
            message=Messages.query.filter( Messages.id == id).first()
            message.state="seen"
            db.session.commit()
            return"state message change 'seen'"
    except Exception as e:
        print(e)
        return make_response(jsonify({'status': 300, 'message': 'Request fail. Please try again'}), 300)