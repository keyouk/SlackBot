import os
from flask import Flask, request, jsonify, abort


app = Flask(__name__)


@app.route('/endpoint', methods=['POST'])
def endpoint():
	if request.method == 'POST':      
		data = request.get_data()
	return data


if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)