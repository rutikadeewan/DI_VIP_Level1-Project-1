
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util



class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello I am Rutika Deewan,\n ')
        self.response.out.write('I am intern at Digirise Infolabs,\n')
        self.response.out.write('I am Third Year Computer Engineering student at MIT.')
        


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()


