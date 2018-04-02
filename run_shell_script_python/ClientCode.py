# Echo client program
import socket
import wakeonlan as wol

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def socket_connection():
    HOST = ''    # The remote host
    PORT = 50007              # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send('Hello, world'.encode())
    data = s.recv(1024)

    print('Received', repr(data.decode()))

def open_socket():
    HOST = ''    # The remote host
    PORT = 50007              # The same port as used by the server
    s.connect((HOST, PORT))

def close_socket():
    s.close()

# Method to do a magic packet send:
def send_magic_packets():
    print("Sending magic packet to Linux machine.")
    wol.send_magic_packet('00.19.D1.91.95.98')


#send_magic_packets()
open_socket()
close_socket()

