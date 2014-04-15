from flask import request, Flask, jsonify, json
app = Flask(__name__)
#TODO: replace tbn() with the real deal
@app.route('/', methods=['GET'])
def get_request():
	return jsonify({'result' : tbn(request.args['input'])})

def tbn(body):
	return 'None'

if __name__ == '__main__':
    app.run()