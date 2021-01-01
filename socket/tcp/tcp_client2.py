import socket

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(("127.0.0.1", 8080))
while True:
    send_data = input("请输入：")
    if send_data == "exit":
        break
    tcp_client.send(send_data.encode("utf-8"))
    # recv_data = tcp_client.recv(1024)
    # print(recv_data.decode("utf-8"))

tcp_client.close()
