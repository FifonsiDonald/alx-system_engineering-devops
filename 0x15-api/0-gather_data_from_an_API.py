#!/usr/bin/python3

"""
Script to retrieve and display TODO list progress for a given employee
using a REST API.
"""

import requests
from sys import argv

if __name__ == "__main__":
	if len(argv) > 1:
		user = argv[1]
		url = "https://jsonplaceholder.typicode.com/"
		req = requests.get("{}users/{}".format(url, user))
		name = req.json().get("name")
		if name is not None:
			jreq = requests.get("{}todos?userId={}".format(url, user)).json()
			allTasks = len(jreq)
			completedTasks = []
			for t in jreq:
				if t.get("completed") is True:
					completedTasks.append(t)
			count = len(completedTasks)
			print("Employee {} is done with tasks ({}/{}):".format(name, count, allTasks))
			for task in completedTasks:
				print("\t {}".format(title.get("title")))
