import socket
import re

def client_service(client_socket):
    request = client_socket.recv(1024).decode("utf-8")
    # print("Request:", request.decode("utf-8"))

    request = request.splitlines()[0]
    ret = re.match(r"[^/]+(/[^ ]*)", request)
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    try:
        f = open("./statics/" + file_name, "rb")
    except:
        header = "HTTP/1.1 404 NOT FOUND\r\n"
        response = header + "\r\n"
        client_socket.send(response.encode("utf-8"))
        client_socket.send("Page Not Found".encode("utf-8"))
    else:
        content = f.read()
        f.close()
        header = "HTTP/1.1 200 OK\r\n"
        response = header + "\r\n"
        client_socket.send(response.encode("utf-8"))
        client_socket.send(content)

    client_socket.close()


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(("", 8080))
    tcp_socket.listen(125)
    while True:
        client_socket, client_addr = tcp_socket.accept()
        client_service(client_socket)

    tcp_socket.close()


if __name__ == "__main__":
    main()