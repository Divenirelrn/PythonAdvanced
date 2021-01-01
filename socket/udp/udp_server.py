import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

local_addr = ("", 8080)
socket_server.bind(local_addr)
recv_data = socket_server.recvfrom(1024)
print(recv_data[0].decode("utf-8"))

socket_server.close()