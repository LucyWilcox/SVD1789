import csv
from votelist import house_votes, senate_votes

def get_votes_names(data):
	votes = {}

	for entry in data:
		data_list = data[entry]
		bill = entry
		for vote in data_list:
			vote = vote.replace(","," ").split()

			if vote[3] == 'Yea':
				name = {}
				person = vote[4]+' '+vote[5]
				if check_dictionary(votes, person) == True:
					name[bill] = True
					votes[person] += [name]
				else:
					name[bill] = True
					votes[person] = [name]
			
			elif vote[3] == 'Nay':
				name = {}
				person = vote[4]+' '+vote[5]
				if check_dictionary(votes, person) == True:
					name[bill] = False
					votes[person] += [name]
				else:
					name[bill] = False
					votes[person] = [name]

			elif vote[3] == 'Not':
				name = {}
				person = vote[5]+' '+vote[6]
				if check_dictionary(votes, person) == True:
					name[bill] = False
					votes[person] += [name]
				else:
					name[bill] = False
					votes[person] = [name]
				
	return votes

def get_data(house_votes):
	data = {}

	for bill in house_votes:
		people = {}
		person = []
		with open(bill, 'rb') as csvfile:
		    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		    for row in spamreader:
		    	person.append(" ".join(row))
    		data.update({bill:person})
    
	return data

def check_dictionary(votes, name):
	if name in votes:
		return True
	else:
		return False

if __name__ == '__main__':
	data = get_data(house_votes)
	print get_votes_names(data)
	
