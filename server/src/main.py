#!/usr/bin/env python
import webapp2
import handler
import signup

class MainHandler(handler.BaseHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/signup', signup.Signup)],
                              debug=True)
