#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
# 暂时有错误
from flask import Flask, request, render_template
from flask.views import View

app = Flask(__name__, template_folder='/templates')


class BaseView(View):
    """

    """

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        if request.method != 'GET':
            return 'UNSUPPORTED'

        context = {'users': self.get_users()}
        return self.render_template(context)


class UserView(BaseView):
    def get_template_name(self):
        return 'users.html'

    def get_users(self):
        return [{'username': 'fake', 'avatar': 'http:www.baidu.com'}]


app.add_url_rule('/users/', view_func=UserView.as_view('userview'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
