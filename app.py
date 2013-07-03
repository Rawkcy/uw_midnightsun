import socket

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    HOST = ''                 # Symbolic name meaning all available interfaces
    PORT = 50007              # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print 'Connected by', addr

    data = conn.recv(1024)
    conn.sendall(data)
    conn.close()

    return '<h1>MIDNIGHT SUN!!!!!</h1><br><br>' + data

if __name__ == '__main__':
    app.run(host="0.0.0.0")
