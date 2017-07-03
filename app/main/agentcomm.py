import socket
import sys

def active_open(host, port):
        address = socket.getaddrinfo(host, port, proto=socket.IPPROTO_TCP)
        client_socket = socket.socket(family = socket.AF_INET,
                                           type=socket.SOCK_STREAM, proto=0)
        try:
            client_socket.connect(address[1][4])
        except ConnectionRefusedError as e:
            print('Connection Refused Try Again Later')
            client_socket.close()
            sys.exit(1)
        return client_socket

def send_buffer(client_socket, msg_buffer, msg_buffer_size):
    total_sent  = 0
    while total_sent < msg_buffer_size:
        bytes_sent = client_socket.send(msg_buffer[total_sent:])
        if bytes_sent == 0:
            raise RuntimeError('socket connection broken')
        total_sent += bytes_sent

def read_line(client_socket):
    bytes_received = ''
    byte = None
    while byte != '\n':
        byte = client_socket.recv(1)
        try:
            byte = byte.decode()
            bytes_received += byte 
        except UnicodeDecodeError as e:
            pass
    return bytes_received

if __name__ == '__main__':
    client_socket = active_open('localhost', 4000)
    message = "16 100"
    send_buffer(client_socket, message.encode('utf-8'), len(message))
    print(read_line(client_socket))
    client_socket.close()
