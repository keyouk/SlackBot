import os
from flask import json
import requests
import operator


# Function returns Top 5 results in stats from getTicket
def sortTicketData(stats):
	items = 5
	total = 0
	sorted_stats = {}

	while items != 0:
		items -= 1

		field = max(stats, key=lambda k: stats[k])
		sorted_stats[field] = stats[field]
		del stats[field]


	for item in sorted_stats:
		total += sorted_stats[item] 

	return sorted_stats, total


# By default, getTickets will get tickets for the last 30 days
# Results are retrieved through pagination. Loop through pages to get all tickets
# "Link" field in headers indicate that there is a next page.
def getTickets(category):	
	stats = {}	
	nextPage = True
	page = 0
	total = 0
	
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
			total += 1
		
		if "link" not in r.headers:
			nextPage = False

	return sortTicketData(stats)