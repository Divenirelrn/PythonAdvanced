import socket
import threading
import re


def worker(socket_client):
    request = socket_client.recv(1024).decode("utf-8")
    request = request.splitlines()[0]
    ret = re.match(r"[^/]+(/[^ ]*)", request)
    if ret:
        file_name = ret.group(1)
        print(file_name)
        if file_name == "/":
            file_name = "/index.html"

    try:
        with open("./statics/" + file_name, "rb") as fp:
            data = fp.read()
    except:
        header = "HTTP/1.1 404 NOT FOUND\r\n"
        body = "Page Not Found"
        response = header + "\r\n" + body
        socket_client.send(response.encode("utf-8"))
    else:
        header = "HTTP/1.1 200 OK\r\n"
        response = header + "\r\n"
        body = data
        socket_client.send(response.encode("utf-8"))
        socket_client.send(body)

    socket_client.close()


def main():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind(("", 8080))
    socket_server.listen(125)
    while True:
        socket_client, client_addr = socket_server.accept()
        t = threading.Thread(target=worker, args=(socket_client,))
        t.start()
        # socket_client.close()

    socket_server.close()



if __name__ == "__main__":
    main()