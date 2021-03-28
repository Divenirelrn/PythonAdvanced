import tornado
import tornado.web
import tornado.ioloop
import tornado.websocket

class IndexHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('index.html')


users = set()
class ChatHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin: str):
        return True

    def open(self, *args, **kwargs):
        """
        客户端与服务端建立连接
        1.连接
        2，握手
        """
        print("coming...")
        users.add(self)

    def on_message(self, message):
        # print(message)
        # message += "李若男"
        content = self.render_string("message.html", msg=message)
        for client in users:
            client.write_message(content)

    def on_close(self):
        users.remove(self)


def run():
    settings = {
        'template_path': 'template',
        'static_path': 'static'
    }

    application = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/chat", ChatHandler)
    ], **settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    run()