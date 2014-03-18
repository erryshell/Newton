#!/usr/bin/env python
import handler
import re
import DB

from google.appengine.ext import db
  
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{6,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
    return email or EMAIL_RE.match(email)

class Signup(handler.BaseHandler):
    
    def get(self):
        self.render("signup-form.html")

    def post(self):
        have_error = False
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        self.email = self.request.get('email')
        
        params = dict(username = self.username,
                      email = self.email)
        
        if not valid_username(self.username):
            params['error_username'] = "Invalid username."
            have_error = True
        
        if not valid_password(self.password):
            params['error_password'] = "Invalid password."
            have_error = True
        elif self.password != self.verify:
            params['error_verify'] = "Passwords do not match."
            have_error = True

        if not valid_email(self.email):
            params["error_email"] = "Invalid email."
            have_error = True

        if have_error:
            self.render('signup-form.html', **params)
        else:
            self.done()
        
    def done(self, *a, **kw):
        raise NotImplementedError

class Register(Signup):
    def done(self):
        u = DB.User.by_name(self.username)
        if u:
            msg = 'Username already exists.'
            self.render('signup-form.html', error_username = msg)
        else:
            u = DB.User.register(self.username, self.password, self.email)
            u.put()
