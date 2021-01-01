
def index():
    with open("./template/index.html", "rb") as fp:
        return fp.read()


def Application(request, start_response):
    start_response("200 OK", [("Content-type", "text/html;charset=utf-8")])
    if request["file_path"] == "/index.py":
        return index()
    else:
        return "Page Not Found".encode("utf-8")