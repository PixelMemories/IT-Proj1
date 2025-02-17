import threading
import time
import random
import os
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

    # Step 4 Author: Richard Li (rl902)
    # send hello
    msg = "HELLO"
    cs.send(msg.encode('utf-8'))

    # get back altered hello
    alter_from_server = cs.recv(100)
    print("[C]: Message received from server: {}".format(alter_from_server.decode('utf-8')))

    # Step 5 Author: Wesley Zhou (wgz4)
    input_file = "in-proj.txt"

    try:
        with open(input_file, 'r') as file:
            for line in file:
                # Send the line to the server
                cs.send(line.strip().encode('utf-8'))  # Strip newline characters
                print(f"[C]: Sent line to server: {line.strip()}")

                # Wait for server confirmation
                confirmation = cs.recv(100).decode('utf-8')
                print(f"[C]: Server confirmation: {confirmation}")
    except FileNotFoundError:
        print(f"[C]: Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"[C]: Error reading file: {e}")

    # close the client socket
    cs.close()
    exit()

if __name__ == "__main__":
    t2 = threading.Thread(name='client', target=client)
    t2.start()

    time.sleep(5)
    print("Done.")
