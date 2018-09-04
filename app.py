import os
from flask import Flask, request, jsonify, abort
from freshdesk import getTickets
from threading import Thread
import requests

app = Flask(__name__)


@app.route('/report', methods=['POST'])
def report():
	available_reports = ['addon', 'category', 'subcategory', 'sdk']
	available_reports2 = ['type','status'] #Ready for Version 2

	text = request.form.get('text', None)
	response_url = request.form.get('response_url', None)
	
	if text not in available_reports:
		return jsonify({'text': "Sorry, you can only create reports for: \n    addon\n    category\n   subcategory\n    sdk\n Please try a different another report.", "mrkdwn": true})

	thread = Thread(target=sendResponse, kwargs={'text': text, 'response_url':response_url})
	thread.start()

	return "Retreiving the top 5 fields with the most tickets in the last 30 days..."


def sendResponse(text, response_url):
	data = getTickets(text)
	SlackMessage = {'text':'Here are the %ss with the largest amount of tickets in the past 30 days:\n\n%s\nTotal:%s' % (text.capitalize(), ''.join('    {}: {}\n'.format(key, val) for key, val in data[0].items()), data[1])}
	
	res = requests.post(response_url, json=SlackMessage)


if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

