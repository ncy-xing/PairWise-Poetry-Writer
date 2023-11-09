"""
Nancy Xing
Assignment: CSCI 3725 M7
Date: 11-2023

Web application for routing API requests to generate poetry given two input words. 
"""

import os, sys
from flask import Flask, render_template, request, send_file, abort,jsonify, session

application = Flask(__name__)

@application.route('/', methods = ['GET', 'POST'])
def index():
    """Load homepage."""
    if request.method == 'GET':
        return render_template('index.html')
    
# Run on local server
if __name__ == '__main__':
    application.debug = True  # Refreshes server when code is changed
    application.run(host='127.0.0.1', port=8000)