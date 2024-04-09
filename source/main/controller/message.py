from source import app
from source.main.function.messages import *



app.add_url_rule('/api/chat/<string:id>',
                 methods=['GET', 'POST', "PATCH", "DELETE"], view_func=messages)

# relationship  chat
#id User
app.add_url_rule('/api/chatblock/<string:id>',
                 methods=['GET', 'POST', 'PATCH'], view_func=blockchat)

#change state message
#id message
app.add_url_rule('/api/message/<string:id>',
                 methods=['GET', 'POST', 'PATCH'], view_func=statemessage)