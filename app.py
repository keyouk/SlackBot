import os
from flask import Flask, request, jsonify, abort
from freshdesk import getTickets


app = Flask(__name__)


@app.route('/report', methods=['POST'])
def report():
	available_reports = ['addon', 'category', 'subcategory', 'sdk']

	if request.method == 'POST':      
		text = request.form.get('text', None)

		if text not in available_reports:
			return jsonify({'text': "Can only create reports with the parameters\naddon\ncategory\nsubcategory\nsdk"})

		data = getTickets(text)
		
		return 'Here are the %ss with the largest amount of tickets:\n\n%s\nTotal:%s' % (text.capitalize(), ''.join('    {}: {}\n'.format(key, val) for key, val in data[0].items()), data[1])