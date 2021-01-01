
url_dict = dict()


def set_url(url):
    def set_func(func):
        url_dict[url] = func
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
    return set_func


@set_url("/index.py")
def index():
    with open("./template/index.html", "rb") as fp:
        return fp.read()


def Application(request, start_response):
    start_response("200 OK", [("Content-type", "text/html;charset=utf-8")])
    url = request["file_path"]
    try:
        func = url_dict[url]
        return func()
    except Exception as e:
        return "Page Not Found".encode("utf-8")