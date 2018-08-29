# coding:utf-8

import logging

from handlers.base_handler import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        # user_records = self.db.person_records
        # user = user_rec

        logging.debug('debug')
        logging.info('info')
        logging.warning('warning')
        logging.error('error')

        # print(self.db.collection_names())