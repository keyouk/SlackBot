import os
import freshdesk
from flask import Flask, request, jsonify, abort



app = Flask(__name__)


@app.route('/report', methods=['POST'])
def report():
	if request.method == 'POST':      
		text = request.form.get('text', None)
		stats = freshdesk.getTickets(text)
		
		return jsonify({"text":stats})



if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)