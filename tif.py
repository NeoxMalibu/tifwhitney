import os
from flask import Flask, url_for, render_template
from jinja2 import Environment, PackageLoader

UPLOAD_FOLDER = '/music'
ALLOWED_EXTENSIONS = set(['mp3', 'wav', 'ogg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#index webpage

@app.route('/', methods=['GET', 'POST'])
def root():
	return render_template('index.html')

#music webpage

@app.route('/music')
def music():
	return render_template('music.html')

#comments page

@app.route('/comments')
def comments():
	return render_template('comments.html')

#contact tif page

@app.route('/contact')
def contact():
	return render_template('contactme.html')
#create tif instance for user controls of website

def tifinstance(login):
	password = "oragothmlp"
	username = "TIFWhitney"
	login = False
	if password == "oragothmlp" and username == "TIFWhitney":
		login = True
	else:
		login = False


if __name__ == '__main__':
	app.run('0.0.0.0', port=int("99"))