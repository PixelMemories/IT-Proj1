import threading
import time
import random

import socket


def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port on which you want to connect to the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    # Receive data from the server
    data_from_server=cs.recv(100)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

    # send hello
    msg = "HELLO"
    cs.send(msg.encode('utf-8'))

    # get back altered hello
    alter_from_server = cs.recv(100)
    print("[C]: Message received from server: {}".format(alter_from_server.decode('utf-8')))

    # start part 5 here. the idea is to read each line of the file one by one in a while loop
    # then for each line (each iteration of the loop) you are gonna send it to the server.
    # somethings to watch out for. you wanna make sure you wait a bit after each line to make sure the server has finished writing
    # if you wanna get really creative, make a way for the server to tell your client the line has been written THEN start the next iteration

    # close the client socket
    cs.close()
    exit()

if __name__ == "__main__":
    t2 = threading.Thread(name='client', target=client)
    t2.start()

    time.sleep(5)
    print("Done.")
