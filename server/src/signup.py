#!/user/bin/env python
import handler
import re

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
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        
        params = dict(username = username,
                      email = email)
        
        if not valid_username(username):
            params['error_username'] = "Invalid username."
            have_error = True
        
        if not valid_password(password):
            params['error_password'] = "Invalid password."
            have_error = True
        elif password != verify:
            params['error_verify'] = "Passwords do not match."
            have_error = True

        if not valid_email(email):
            params["error_email"] = "Invalid email."
            have_error = True

        if have_error:
            self.render('signup-form.html', **params)
        else:
            self.redirect('/home')
