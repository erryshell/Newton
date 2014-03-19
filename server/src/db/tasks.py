#!/usr/bin/env python
from utils import *
from google.appengine.ext import db

class Tasks(db.Model):
    name = db.StringProperty(required = True)
    algorithm = db.StringProperty(required = True)
    description = db.TextProperty()
    population = db.IntegerProperty(required = True)
    max_gen = db.IntegerProperty(required = True)
    cur_gen = db.IntegerProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    updated = db.DateTimeProperty(auto_now = True)

    def render_brief(self):
        return render_str("task_brief.html", t = self)

    @classmethod
    def by_user_key(cls, user_key):
        return Tasks(parent=user_key)

    @classmethod
    def create(cls,
               user_key, 
               name, 
               algorithm, 
               population, 
               max_gen, 
               description = None):
        return Tasks(parent = user_key,
                     name = name,
                     algorithm = algorithm,
                     population = population,
                     max_gen = max_gen,
                     cur_gen = 0,
                     description = description)
