import socket
import time
import re


def client_service(socket_client, request):
    request = request.splitlines()[0].decode("utf-8")
    ret = re.match(r"[^/]+(/[^ ]*)", request)
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    print(file_name)

    try:
        with open("./statics/" + file_name, "rb") as fp:
            data = fp.read()
    except Exception as e:
        header = "HTTP/1.1 404 NOT FOUND\r\n"
        body = "Page Not Found"
        response = header + "\r\n" + body
        socket_client.send(response.encode("utf-8"))
    else:
        body = data
        header = "HTTP/1.1 200 OK\r\n"
        header += "Content-Length: %d\r\n" % len(body)
        header += "\r\n"
        response = header.encode("utf-8") + body
        socket_client.send(response)


def main():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind(("", 8080))
    socket_server.listen(125)
    socket_server.setblocking(False)
    socket_list = list()
    while True:
        time.sleep(0.5)
        try:
            socket_client, client_addr = socket_server.accept()
        except:
            print("No request")
        else:
            socket_client.setblocking(False)
            socket_list.append(socket_client)

        for socket_client in socket_list:
            try:
                request = socket_client.recv(1024)
            except:
                pass
            else:
                if request:
                    client_service(socket_client, request)
                else:
                    socket_list.remove(socket_client)
                    socket_client.close()

    socket_server.close()


if __name__ == "__main__":
    main()