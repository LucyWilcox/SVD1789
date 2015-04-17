import csv
from votelist import house_votes, senate_votes

# with open('congress_votes_1-1_h35.csv', 'rb') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print " ".join(row)




for vote in house_votes:
	with open(vote, 'rb') as csvfile:
	    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	    for row in spamreader:
	        print " ".join(row)