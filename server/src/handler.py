#!/usr/bin/env python
import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        #use jinja to process the html (do escaping, subsitution, etc.)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
