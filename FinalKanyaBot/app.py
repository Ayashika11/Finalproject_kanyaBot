from flask import Flask, render_template, redirect, url_for, request
import requests
from flask import *

# create the application object
app = Flask(__name__)

@app.route('/index', methods = ['POST', 'GET'])
def index():
    return render_template('index.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
