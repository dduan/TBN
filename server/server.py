from flask import request, Flask, jsonify, json

import os
app = Flask(__name__, static_folder='../')

@app.route('/')
def index():
	return app.send_static_file('client/index.html')

@app.route('/client/<path:path>')
def static_proxy(path):
	return app.send_static_file(os.path.join('client', path))
#TODO: replace tbn() with the real deal
@app.route('/api', methods=['GET'])
def get_request():
	return jsonify({'result' : tbn(request.args['input'])})

def tbn(body):
	return 'None'

if __name__ == '__main__':
    app.run()