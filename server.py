from flask import Flask, render_template, request
import csv
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/<string:html_page>')
def page(html_page):
	return render_template(html_page)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST' and request.form.getlist('human'):
    	email = request.form.get('email')
    	message = request.form.get('message')
    	with open('database.csv', 'a', newline = '') as database:
    		writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    		writer.writerow([email,message])
    	return render_template('/contact-success.html')
    else:
    	return 'try again'

