#!/usr/bin/env python
import handler
import DB

class Login(handler.BaseHandler):

    def get(self):
        self.render('login-form.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        
        u = DB.User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/home')
        else:
            msg = "invalid login"
            self.render('login-form.html', error = msg)
    
