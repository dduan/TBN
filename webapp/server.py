from flask import request, Flask, jsonify, json

import os
app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
	return app.send_static_file('static/index.html')

#TODO: replace tbn() with the real deal
@app.route('/api', methods=['GET'])
def get_request():
	return jsonify({'result' : tbn(request.args['input'])})

def tbn(body):
	return 'None'

if __name__ == '__main__':
    app.run()