#encoding=utf-8
import socket
import select
import re


def client_service(socket_client, request):
    request = request.decode("utf-8")
    request = request.splitlines()[0]
    ret = re.match(r"[^/]+(/[^ ]*)", request)
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    try:
        with open(file_name, "rb") as fp:
            data = fp.read()
    except Exception as e:
        header = "HTTP/1.1 404 NOT FOUND\r\n"
        body = "Page Not Found"
        response = header + "/r/n" + body
        socket_client.send(response.encode("utf-8"))
    else:
        header = "HTTP/1.1 200 OK\r\n"
        header += "Content-Length: %d\r\n" % len(data)
        header += "\r\n"
        body = data
        response = header.encode("utf-8") + body
        socket_client.send(response)


def main():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind(("", 8080))
    socket_server.listen(125)
    print(select.__dict__)
    epl = select.epoll()
    epl.register(socket_server.fileno(), select.EPOLLIN)
    fileno_dict = dict()
    while True:
        fileno_list = epl.poll()
        for fd, event in fileno_list:
            if fd == socket_server.fileno():
                socket_client, _ = socket_server.accept()
                epl.register(socket_client.fileno(), select.EPOLLIN)
                fileno_dict[socket_client.fileno()] = socket_client
            elif event == select.EPOLLIN:
                socket_client = fileno_dict[fd]
                request = socket_client.recv(1024)
                if request:
                    client_service(socket_client, request)
                else:
                    socket_client.close()
                    epl.unregister(fd)
                    del fileno_dict[fd]


if __name__ == "__main__":
    main()