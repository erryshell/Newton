#!/usr/bin/env python
from utils import *
from google.appengine.ext import db

class Task(db.Model):
    name = db.StringProperty(required = True)
    algorithm = db.StringProperty(required = True)
    description = db.TextProperty()
    population = db.IntegerProperty(required = True)
    max_gen = db.IntegerProperty(required = True)
    cur_gen = db.IntegerProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    updated = db.DateTimeProperty(auto_now = True)

    def render_item(self):
        return render_str("task_item.html", t = self)

    @classmethod
    def by_user_key(cls, user_key):
        tasks = Task.all().filter('parent =', user_key).get()
        if tasks:
            return tasks.order('-updated')

    @classmethod
    def create(cls,
               user_key, 
               name, 
               algorithm, 
               population, 
               max_gen, 
               description = None):
        return Task(parent = user_key,
                     name = name,
                     algorithm = algorithm,
                     population = population,
                     max_gen = max_gen,
                     cur_gen = 0,
                     description = description)
