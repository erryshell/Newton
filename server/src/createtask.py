#!/usr/bin/env python
import handler
import re
import DB

from google.appengine.ext import db
  
class CreateTask(handler.BaseHandler):
    
    def get(self):
        self.render("newtask.html")

    def post(self):
        have_error = False
        self.taskname = self.request.get('taskname')
        self.description = self.request.get('description')
        self.algorithm = self.request.get('algorithm')
        self.population = self.request.get('population')
        self.generation = self.request.get('generation')
        
        params = dict(taskname = self.taskname,
                      description = self.description,
                      algorithm = self.algorithm,
                      population = self.population,
                      generation = self.generation)

        self.have_error = False
        if self.have_error:
            self.render('signup-form.html', **params)
        else:
            self.done()
        
    def done(self, *a, **kw):
        raise NotImplementedError
