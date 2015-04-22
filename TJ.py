import csv
from votelist import house_votes, senate_votes

def check_dictionary(votes, name):
	if name in votes:
		return True
	else:
		return False

def get_votes_names(data):
	name = {}
	for entry in data:
		votes = {}
		data_list = data[entry]
		bill = entry
		for vote in data_list:
			print vote
			vote = vote.replace(","," ").split()
			if vote[2] == 'Yea':
				person = str(vote[3]+' '+vote[4])
				if check_dictionary(votes, person) == True:
					name[bill] = True
				else:
					name[bill] = True
					votes.update({person:name})	
			
			elif vote[2] == 'Nay':
				
				person = vote[3]+' '+vote[4]
				if check_dictionary(votes, person) == True:
					name[bill] = False
				else:
					name[bill] = False
					votes.update({person:name})	

			elif vote[2] == 'Not':
				
				person = vote[4]+' '+vote[5]
				if check_dictionary(votes, person) == True:
					name[bill] = False
				else:
					name[bill] = False
					votes.update({person:name})	

	return votes

def get_data(votes):
	data = {}

	for bill in votes:
		people = {}
		person = []
		with open(bill, 'rb') as csvfile:
		    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		    for row in spamreader:
		    	person.append(" ".join(row))
    		data.update({bill:person})
    
	return data


def create_voter_list(house_dict):
	"""Generates a list of voters names """
	voters = []
	for key in sorted(house_dict):
		voters.append(key)
	return voters

if __name__ == '__main__':
	print senate_votes
	data = get_data(senate_votes)
	senate_data = get_votes_names(data)
	print senate_data
	print create_voter_list(senate_data)