import tornado.ioloop
from .handlers.main_handler import MainHandler
from .handlers.image_handler import ImageHandler


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/img/?", ImageHandler),
        (r"/img/([^/]+)?", ImageHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()