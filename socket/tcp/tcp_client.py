import socket

#创建套接字
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#连接主机
dst_addr = ("127.0.0.1", 8080)
socket_client.connect(dst_addr)

#发送数据
socket_client.send("你好".encode('utf-8'))

#接受返回
recv_data = socket_client.recv(1024)
print(recv_data.decode('utf-8'))

#关闭套接字
socket_client.close()



