import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dst_addr = ("127.0.0.1", 8080)

socket_client.sendto("你好".encode("utf-8"), dst_addr)

socket_client.close()