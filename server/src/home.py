#!/usr/bin/env python
import handler

class Home(handler.BaseHandler):
    
    def get(self):
        if self.user:
            params = dict(username = self.user.name)
            #TODO:
            #restore tasks in memcache
            tasks = Tasks.by_user_key(self.user).order('-updated')
            if tasks:
                params["tasks"] = tasks
            else:
                params["error"] = "You currently have no tasks."
            self.render("home.html", username = self.user.name)
        else:
            self.redirect('/signup')
