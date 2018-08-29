# coding:utf-8

import os

config = {
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'template'),
    # base64.b64encode(uuid.uuid4().bytes +  uuid.uuid4().bytes)
    'cookie_secret': 'q6cjSWRfRBaoHHGKAvNf7am1mk5iC0WUo1zA0HPwzFs=',
    'xsrf_cookies': 'OFbGYpi3QhyDzymV7DYlloZaV2tUdUt1tMXyXL8ikdo=',
    'debug': True,
}

mlab_options = dict(
    MONGO_URI = 'mongodb://adrianacmy:adrianacmy321@ds111622.mlab.com:11622/tornado-python'

)

mysql_options = dict(
    host = '',
    databse = '',
    user = '',
    password = ''
)


redis_options = dict(
    host = '',
    port = ''
)

log_file = os.path.join(os.path.dirname(__file__), 'logs/log')