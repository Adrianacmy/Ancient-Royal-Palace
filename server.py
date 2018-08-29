# coding:utf-8


import tornado.web
import tornado.ioloop
import tornado.httpserver

from pymongo import MongoClient

from tornado.web import RequestHandler
from tornado.options import define, options

from urls import handlers
import config

define('port', type=int, default=8000, help='run server on this port')


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.mlab_client = MongoClient(
            config.mlab_options['MONGO_URI'],
            connectTimeoutMS=30000,
            socketTimeoutMS=None,
            socketKeepAlive=True
        )
        self.db = self.mlab_client.get_database('tornado-python')


def main():
    options.logging = 'warning'
    options.log_file_prefix = config.log_file
    tornado.options.parse_command_line()

    app = Application(
        handlers, **config.config
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
