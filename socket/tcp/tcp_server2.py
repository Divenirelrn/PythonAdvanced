import socket

#创建套接字
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_addr = ("", 8080)
socket_server.bind(local_addr)
socket_server.listen(5)
socket_client, socket_addr = socket_server.accept()
while True:
    recv_data = socket_client.recv(1024)
    if recv_data:
        print(recv_data.decode("utf-8"))
        socket_client.send("你好，有什么可以帮您".encode("utf-8"))
    else:
        socket_client.close()
        break

socket_server.close()
