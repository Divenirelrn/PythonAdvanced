import socket
import multiprocessing as mp
import re, os
# from dynamic.mini_frame import Application

import sys


class WSGIServer(object):
    def __init__(self, port, application, static_path):
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_server.bind(("", port))
        self.socket_server.listen(125)
        self.application = application
        self.static_path = static_path

    def run(self):
        while True:
            socket_client, client_addr = self.socket_server.accept()
            p = mp.Process(target=self.worker, args=(socket_client,))
            p.start()
            socket_client.close()

        self.socket_server.close()

    def worker(self, socket_client):
        request = socket_client.recv(1024).decode("utf-8")
        request = request.splitlines()[0]
        ret = re.match(r"[^/]+(/[^ ]*)", request)
        if ret:
            file_name = ret.group(1)
            print(file_name)
            if file_name == "/":
                file_name = "/index.html"

        if not file_name.endswith(".py"):
            try:
                with open(self.static_path + file_name, "rb") as fp:
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
        else:
            request_ = {"file_path": file_name}
            body = self.application(request_, self.start_response)
            header = "HTTP/1.1 " + self.status + "\r\n"
            for ele in self.header:
                header += ele[0] + ": " + ele[1] + "\r\n"
            header += "server: mini_frame\r\n"
            response = (header + "\r\n").encode("utf-8") + body
            socket_client.send(response)
        socket_client.close()

    def start_response(self, status, header):
        self.status = status
        self.header = header

#D:\files\AI\Projects\python_advanced\web_frame
def main():
    if len(sys.argv) == 2:
        try:
            port = int(sys.argv[1])
        except Exception as e:
            print("Port error")
            return
    else:
        print("Args error")
        return
    with open("./config/mini_frame.conf", "r") as fp:
        conf = eval(fp.read())

    frame_path = conf["frame_path"]
    static_path = conf["static_path"]

    sys.path.append("./dynamic")
    frame = __import__(frame_path)
    app = getattr(frame, "Application")

    server = WSGIServer(port, app, static_path)
    server.run()


if __name__ == "__main__":
    main()