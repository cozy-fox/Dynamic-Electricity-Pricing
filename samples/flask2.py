#This is reference for url_for
from flask import Flask
from flask import url_for

app = Flask(__name__)



@app.route('/')
def index():
	staticFilename = url_for('static', filename='default.css')
	
	html = '<html><head><title>Demo Static File</title><link rel="stylesheet" type="text/css" href="' + staticFilename + '"></head><body><h1 class="special">This is a Special Heading</h1></body></html>'
	
	return html
