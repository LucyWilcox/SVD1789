import csv
from votelist import house_votes, senate_votes

def get_votes_names(data,bill):
	data = data[1:len(data)]
	name = {}
	votes = {}

	for vote in data:
		vote = vote.replace(","," ").split()

		if vote[3] == 'Yea':
			if check_dictionary(votes, vote[4]+' '+vote[5]) == True:
				vote = True
				name.update({bill:vote})
			else:
				votes.update({vote[4]+' '+vote[5]: {bill:True}})
				
		elif vote[3] == 'Nay':
			if check_dictionary(votes, vote[4]+' '+vote[5]) == True:
				vote = True
				name.update({bill:vote})
			else:
				votes.update({vote[4]+' '+vote[5]: {bill:False}})

		elif vote[3] == 'Not':
			if check_dictionary(votes, vote[5]+' '+vote[6]) == True:
				vote = True
				name.update({bill:vote})
			else:
				votes.update({vote[5]+' '+vote[6]: {bill:False}})
				
	return votes

def get_data(house_votes):
	data = {}
	for vote in house_votes:
		with open(vote, 'rb') as csvfile:
		    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		    for row in spamreader:
		        data.update({vote:(" ".join(row)})
		        
	return data

def check_dictionary(votes, name):
	if name in votes:
		return True
	else:
		return False

if __name__ == '__main__':
	bill = 'bill'
	data = get_data(house_votes)
	print get_votes_names(data,bill)
