# Brian Mann
# 5/24/2016

# This file contains the necessary to code to setup a basic server, using classes defined in data.py to properly handle all requests


import cherrypy
from data import FoursquareController
from data import TwitterController
from data import InstagramController

class OptionsController:
	def OPTIONS(self, *args, **kwargs):
		return ""

def CORS():
	cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
	cherrypy.response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
	cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"

def start_service():
	dispatcher = cherrypy.dispatch.RoutesDispatcher()
	foursquareController = FoursquareController()
	twitterController = TwitterController()
	instagramController = InstagramController()
	optionsController = OptionsController()

	dispatcher.connect('foursquare_post', '/foursquare/', controller=foursquareController, action = 'POST', conditions=dict(method=['POST']))

	dispatcher.connect('twitter_post', '/twitter/', controller=twitterController, action = 'POST', conditions=dict(method=['POST']))

	dispatcher.connect('instagram_post', '/instagram/', controller=instagramController, action = 'POST', conditions=dict(method=['POST']))

	dispatcher.connect('foursquare_option', '/foursquare/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))

	dispatcher.connect('twitter_option', '/twitter/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))

	dispatcher.connect('instagram_option', '/instagram/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))

	conf = {
		'global': {
			'server.socket_host': '0.0.0.0',
			'server.socket_port': 8008
		},
		'/': {
			'request.dispatch': dispatcher,
			'tools.CORS.on': True,
		}
	}

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)

if __name__ == '__main__':
	cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
	start_service()
