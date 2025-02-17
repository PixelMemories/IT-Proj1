import threading
import time
import random
import os
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

    # Part 4 Author: Richard Li (rl902)
    # recv hello
    data_from_client=csockid.recv(100)
    print("[S]: Got the Message: {}".format(data_from_client.decode('utf-8')))

    # do something to hello and send back
    alter = reverse_and_lowercase(data_from_client)
    csockid.send(alter)

    # Part 5 Author: Wesley Zhou (wgz4)
    output_file = "out-proj.txt"

    try:
        with open(output_file, 'w') as file:
            while True:
                # Receive a line from the client
                line = csockid.recv(200).decode('utf-8')
                if not line:
                    break  # Exit loop if no more data is received

                print(f"[S]: Received line from client: {line}")

                # Reverse and lowercase the line
                processed_line = reverse_and_lowercase(line.encode('utf-8')).decode('utf-8')
                print(f"[S]: Processed line: {processed_line}")

                # Write the processed line to the output file
                file.write(processed_line + '\n')

                # Send confirmation back to the client
                csockid.send("ACK".encode('utf-8'))  # Acknowledgment
    except Exception as e:
        print(f"[S]: Error writing to file: {e}")
    # reverse_and_lowecase method on the data. Then you write it into an output file called "out-proj.txt"

    # Close the server socket
    ss.close()
    exit()

def reverse_and_lowercase(input_string):
    reversed_string = input_string[::-1]  # Reverses the string
    return reversed_string.swapcase()  # Converts to lowercase

if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()
