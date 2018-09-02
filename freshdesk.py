import os
from flask import Flask, request, jsonify, abort, json
import requests


# Must retrieve tickets by pagination.
# Runs for loop through pages, retrieving tickets asynchronously
# Default grabs tickets for the last 30 days
def getTickets(category):	
	stats = {}	

	nextPage = True
	page = 0
	while nextPage != False:
		page += 1
		r = requests.get(('https://pubnub.freshdesk.com/api/v2/tickets?per_page=100&page=%s') % page, 
							headers={'Authorization':'MFdEUnh2dE1OY3R6MEExRTBacXY6WAo='}) 
		data = r.json()
		
		for ticket in range(len(data)):
			field = data[ticket]['custom_fields'][category]
			if field == None:
				continue 

			if field not in stats:
				stats[field] = 0
		
			stats[field] += 1
		
		if "link" not in r.headers:
			nextPage = False

	return stats


# def getTicket(category):
# 	stats = {}
# 	r = requests.get(('https://pubnub.freshdesk.com/api/v2/tickets?per_page=100&page=1'), 
# 							headers={'Authorization':'MFdEUnh2dE1OY3R6MEExRTBacXY6WAo='}) 
# 	data = r.json()

# 	for ticket in range(len(data)):
# 		field = data[ticket]['custom_fields'][category]
# 		if field == None:
# 			continue
# 		if field not in stats:
# 			stats[field] = 0
		
# 		stats[field] += 1

# 	print stats

if __name__ == '__main__':
	getTickets('sdk')