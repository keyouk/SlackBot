import os
from flask import Flask, request, jsonify, abort


app = Flask(__name__)
webhook = "insert webhook here"


@app.route('/hello', methods=['GET','POST'])
def hello():
	if request.method == 'POST':      
		data = request.form.get()
				
		return ({"text": data})



if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)