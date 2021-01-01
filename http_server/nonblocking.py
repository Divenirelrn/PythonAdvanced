import socket
import time


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
                print("No data")
            else:
                if request:
                    print(request)
                else:
                    socket_list.remove(socket_client)
                    socket_client.close()

    socket_server.close()


if __name__ == "__main__":
    main()