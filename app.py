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
	SlackMessage = { "attachments":[
			{'text':''.join('{}: {}\n'.format(key, val) for key, val in data[0].items())}
		]
	}
	
	r = requests.post(response_url, json=SlackMessage)


