#!/usr/bin/env python
import handler

class Logout(handler.BaseHandler):

    def get(self):
        self.logout()
        self.redirect('/')
    
