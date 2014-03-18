#!/usr/bin/env python
import webapp2
import handler
import signup
import login
import logout
import home

class MainHandler(handler.BaseHandler):
    def get(self):
        self.render("index.html")

app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/home', home.Home),
                               ('/signup', signup.Register),
                               ('/login', login.Login),
                               ('/logout', logout.Logout)],
                              debug=True)
