from source import socketIo, app
from source.socket import *
from source.main.controller import *


if __name__ == '__main__':
    socketIo.run(app, host="0.0.0.0", port=1357)
    #  ssl_context=('/etc/ssl/iudi_online.crt','/etc/ssl/iudi.online.key'))
