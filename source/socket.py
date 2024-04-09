from flask_socketio import SocketIO
from flask_socketio import emit,join_room,leave_room
from flask import request
from source import socketIo,db,connected_clients
from source.main.model.messages import Messages
from source.main.model.relationships import Relationships
from datetime import datetime
from sqlalchemy import and_
import smtplib
import eventlet

@socketIo.on('online')
def online(data):
    fl=True
    print('client connect')
    for obj in connected_clients:
        if obj.get('id') == data['user']['id']:
            fl=False
            break
    if(fl==True):
        connected_clients.append(data['user'])
    print(connected_clients)
    # Gửi danh sách client đang kết nối cho client vừa kết nối thành công
    emit('online', {'online':connected_clients})
@socketIo.on('offline')
def offline(client_id ):
    print(f'user :{client_id}')
    print('client offline')
    for obj in connected_clients:
        if obj.get('id') == client_id:
            connected_clients.remove(obj)
            print(connected_clients)
            break
    
    
    # Gửi danh sách client đang kết nối cho client vừa kết nối thành công
    emit('offline', {'online':connected_clients})
@socketIo.on('connect')
def connected():
   
    client_id = request.sid
    
    print(connected_clients)
    emit('connect',  {'online':connected_clients})
    


@socketIo.on('disconnected')
def disconnected():
    print('User disconnected')
    emit("disconnected", f"User {request.sid} is connected", broadcast=True)

@socketIo.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    print("join")


@socketIo.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)
    print("leave")

@socketIo.on('chat_group')
def chat_group(data):
    room=data['room']
    message = data['data']
    print(message,data)
    newChat=Chats(idGroup=room,sendAt=datetime.strptime(
                message['sendAt'], "%d/%m/%Y %H:%M %p %z"),idSend=message["idSend"],type=message['type'])
    if(newChat.type=="image" or newChat.type=="icon-image" or newChat.type=="muti-image"):
        newChat.image=message['metaData']
    else:
        newChat.text=message['content']
    db.session.add(newChat)
    db.session.commit()
    message['sendAt']=str(newChat.sendAt)
     # Lấy thời gian hiện tại
    emit('chat_group',message, room=room)


# chat 1vs1

@socketIo.on('join_room')
def handle_join_room(data):
    room = data['room']
    join_room(room)
    print(' ')
    # Truy vấn tin nhắn từ cơ sở dữ liệu và gửi chúng đến người dùng
    messages = Messages.query.filter((Messages.idSend == room) | (Messages.idReceive == room)).all()
    for message in messages:
        emit('message', {'sender': message.sender, 'content': message.content})

# @socketIo.on("private message", ({ content, to }) => {
#   socket.to(to).emit("private message", {
#     content,
#     from: socket.id,
#   });
# });

@socketIo.on('send_message')
def handle_send_message(data):
    try:
        room=data['room']
        message = data['data']
        print(message,data)
        user1 = Relationships.query.filter(
                    (Relationships.idSend == message["idSend"]) & (Relationships.idReceive == message['idReceive'] )
                ).first()
        user2 = Relationships.query.filter((Relationships.idReceive == message["idSend"]) & (Relationships.idSend == message['idReceive'] )
                ).first()
        if(user1.relation == True and user2.relation == True):
            newChat=Messages(sendAt=datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S %z"),idSend=message["idSend"],idReceive=message["idReceive"],room=room,type=message['type'])        
            if(newChat.type=="image" or newChat.type=="icon-image" or newChat.type=="muti-image"):           
                newChat.img=message['data']
            else:
                newChat.text=message['content']
            
            db.session.add(newChat)       
            db.session.commit() 
            
            emit('send_message',message, room=room)
            eventlet.sleep(900)
            pushemail(newChat.id) 
            # scheduler.add_job(pushemail, 'interval', minutes=1, newChat.id)

        else:
            print("you are banned from chatting")
            emit('send_message',f"you are banned from chatting", room=room)
        # ,state=message["state"]
    except Exception as e:
    # Log the error message
        print("SQL Error:", str(e))
