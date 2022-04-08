import webapp2
import os
import urllib
from google.appengine.ext.webapp import template

class BaseHandler(webapp2.RequestHandler):
  def render_template(self, filename, **template_args):
     path = os.path.join(os.path.dirname(__file__), filename)
     self.response.write(template.render(path, template_args))

class IndexHandler(BaseHandler):
  def get(self):
    self.render_template('index.html', name=self.request.get('name'))

application = webapp2.WSGIApplication([
    ('/', IndexHandler),
], debug=True)
#class MainPage(webapp2.RequestHandler):
#    def get(self):
#        path = os.path.join(os.path.dirname(_file_), "index.html")
#        self.response.out.write(template.render(path, context))
        
#app = webapp2.WSGIApplication([('/', MainPage)],  debug=True)
#STACK OVERFLOW