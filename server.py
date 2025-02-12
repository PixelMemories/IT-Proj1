import threading
import time
import random

import socket

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    # send a intro message to the client.  
    msg = "Welcome to CS 352!"
    csockid.send(msg.encode('utf-8'))

    # recv hello
    data_from_client=csockid.recv(100)
    print("[S]: Got the Message: {}".format(data_from_client.decode('utf-8')))

    # do something to hello and send back
    alter = reverse_and_lowercase(data_from_client)
    csockid.send(alter)

    # Close the server socket
    ss.close()
    exit()

def reverse_and_lowercase(input_string):
    reversed_string = input_string[::-1]  # Reverses the string
    return reversed_string.lower()  # Converts to lowercase

if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()
