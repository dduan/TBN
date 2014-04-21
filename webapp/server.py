from flask import request, Flask, jsonify
from calcneue.document import Document

import os
app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api', methods=['GET'])
def get_request():
    doc = Document(request.args['input'])
    return jsonify({'result' : doc.evaluate()})

if __name__ == '__main__':
    app.run()
