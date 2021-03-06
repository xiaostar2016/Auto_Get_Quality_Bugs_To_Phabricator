#!/usr/bin/env python
# coding:utf-8
import cPickle
import json

import requests

history_path = "./AutoTool/history_file/"
web_message_path = "./AutoTool/web_files/web_message.json"


class UseManiphest:
    def __init__(self):
        with open(web_message_path, 'r') as load_f:
            load_dict = json.load(load_f, encoding='UTF-8')
        self.headers = load_dict['headers']
        self.index_url = load_dict['index_url']
        self.maniphest = 'maniphest/'

    def load_session(self):
        with open(history_path + 'cookies', 'rb') as f:
            # headers = cPickle.load(f)
            cookies = cPickle.load(f)
        return cookies

    def enter_maniphest(self):
        session = requests.session()
        get_url = bytes(self.index_url) + bytes(self.maniphest)
        maniphest_page = session.get(get_url, headers=self.headers, cookies=self.load_session())
        maniphest_content = maniphest_page.content

        print '\n'
        print '\n'
        print '-------------------------------maniphest_content--------------------------------------'
        print maniphest_content
