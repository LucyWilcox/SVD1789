import csv
from votelist import house_votes, senate_votes
from numpy import matrix



# with open('congress_votes_1-1_h35.csv', 'rb') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print " ".join(row)

class Voter(object):
	__init__(self, name, location, voting_record):
		self.name = name
		self.location = location
		self.voting_record = voting_record



for vote in house_votes:
	with open(vote, 'rb') as csvfile:
	    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	    for row in spamreader:
	        print " ".join(row)