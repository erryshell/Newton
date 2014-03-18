#!/usr/bin/env python
import handler

class Home(handler.BaseHandler):
    
    def get(self):
        if self.user:
            self.render("home.html", username = self.user.name)
        else:
            self.redirect('/signup')
