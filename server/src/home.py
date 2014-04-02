#!/usr/bin/env python
import handler
import DB

class Home(handler.BaseHandler):
    
    def get(self):
        if self.user:
            params = dict(username = self.user.name)
            #TODO:
            #restore tasks in memcache
            tasks = DB.Task.by_user_key(self.user)
            if tasks:
                params["tasks"] = tasks
            else:
                params["error"] = "You currently have no tasks."
            self.render("home.html", **params)
        else:
            self.redirect('/signup')
