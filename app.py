from flask import Flask
from conf import settings

application = Flask(__name__)

@application.route("/")
def landing():
	return '<h1> Some formatted html, blah blah, make a template</h1>'

if __name__ == '__main__':
	application.run(host=settings.HOST)
	
