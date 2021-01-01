import socket

#创建套接字
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#绑定端口,监听请求
local_addr = ("", 8080)
socket_server.bind(local_addr)
socket_server.listen(5)

#接受连接，创建客户端套接字
client_socket, client_addr = socket_server.accept()

#接受请求
recv_data = client_socket.recv(1024)
print(recv_data.decode('utf-8'))

#返回数据
client_socket.send("您好，有什么可以帮您".encode("utf-8"))

#关闭套接字
client_socket.close()

