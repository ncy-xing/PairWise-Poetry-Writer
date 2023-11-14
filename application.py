"""
Nancy Xing
Assignment: CSCI 3725 M7
Date: 11-2023

Web application for routing API requests to generate poetry given two input words. 
"""

import os, sys
from flask import Flask, render_template, request, send_file, abort, jsonify, session

application = Flask(__name__)

# Change variable notation for angularJS compatibility
jinja_options = application.jinja_options.copy()
jinja_options.update(dict(
    block_start_string='<%',
    block_end_string='%>',
    variable_start_string='%%',
    variable_end_string='%%',
    comment_start_string='<#',
    comment_end_string='#>',
))
application.jinja_options = jinja_options


@application.route('/', methods = ['GET'])
def index():
    """Load homepage."""
    if request.method == 'GET':
        return render_template('index.html')
    
@application.route('/generate-poem', methods = ['POST'])
def generate_poem():
    """Generate and return poem given two inspiring words."""
    word_1 = request.args.get("word-1")
    word_2 = request.args.get("word-2")
    return jsonify("This is a test poem")
    
# Run on local server
if __name__ == '__main__':
    application.debug = True  # TODO Refreshes server when code is changed
    application.run(host='127.0.0.1', port=8000)