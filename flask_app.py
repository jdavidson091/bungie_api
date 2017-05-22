import requests
import pdb
import json
from flask import Flask
from conf import settings

app = Flask(__name__)

@app.route("/")
def landing():
	return '<h1> Some formatted html, blah blah, make a template</h1>'


@app.route('/test')
def test():
	headers = {'X-API-KEY': 'c901eed646564c589ef870fec494ae43'}
	url = 'https://www.bungie.net/platform/Destiny/Manifest/InventoryItem/1274330687/'
	r = requests.get(url, headers=headers)
	inventory_item = r.json()
	#response = json.dumps(inventory_item, 
	#					  #sort_keys = True, 
	#					  indent = 4, 
	#					  separators = (',', ': '))
	
	return app.make_response(json.dumps(inventory_item))
	#return render_template('json_pretty.html', response=response)

if __name__ == '__main__':
	app.run(host=settings.HOST)
	
