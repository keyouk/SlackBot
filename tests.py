import os
from flask import Flask, request, jsonify, abort
from freshdesk import getTickets


app = Flask(__name__)


@app.route('/report', methods=['POST'])
def report():
	if request.method == 'POST':      

		text = request.form.get('text', None)
		available_reports = ['addon', 'category', 'subcategory', 'sdk']
		
		if text not in available_reports:
			return jsonify({'text': "*Sorry, you can only create reports for:* \n    addon\n    category\n   subcategory\n    sdk"})


	data = getTickets(text)
	SlackMessage = { "attachments":[
			{'text':''.join('{}: {}\n'.format(key, val) for key, val in data[0].items())}
		]
	}
	return jsonify(SlackMessage)


if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)