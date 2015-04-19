import csv
from votelist import house_votes, senate_votes, house_voters


def get_votes_names(data, house_voters):
	full_dict = dict.fromkeys(house_voters)
	for bill in data:
		for vote in data[bill]:
			vote = vote.replace(","," ").split()
			if vote[3] == 'Yea':
				person = str(vote[4]+' '+vote[5])
				if full_dict[person] == None:
					full_dict[person] = [(bill, True)]
				else:
					full_dict[person].append((bill, True))
			
			elif vote[3] == 'Nay':
				
				person = vote[4]+' '+vote[5]
				if full_dict[person] == None:
					full_dict[person] = [(bill, False)]
				else:
					full_dict[person].append((bill, False))

			elif vote[3] == 'Not':
				
				person = vote[5]+' '+vote[6]
				if full_dict[person] == None:
					full_dict[person] = [(bill, False)]
				else:
					full_dict[person].append((bill, False))

	return full_dict


def to_complete_dict(house_dict):
	for key, value in house_dict.iteritems():
		house_dict[key] = dict(value)

	return house_dict


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


if __name__ == '__main__':
	data = get_data(house_votes)
	house_dict = get_votes_names(data, house_voters)
	final_dict = to_complete_dict(house_dict)
	print final_dict
	#print house_dict
	#list_of_names = create_voter_list(house_dict)
	#names = name_dictionary(list_of_names)
	#print vote_dictionary(data,names)

# def check_dictionary(votes, name):
# 	if name in votes:
# 		return True
# 	else:
# 		return False

# def get_votes_names(data):
# 	name = {}
# 	votes = {}
# 	for entry in data:
# 		bill = entry
# 		for vote in data[entry]:
# 			vote = vote.replace(","," ").split()
# 			if vote[3] == 'Yea':
# 				person = str(vote[4]+' '+vote[5])
# 				if check_dictionary(votes, person) == True:
# 					name[bill] = True
# 				else:
# 					name[bill] = True
# 					votes.update({person:name})	
			
# 			elif vote[3] == 'Nay':
				
# 				person = vote[4]+' '+vote[5]
# 				if check_dictionary(votes, person) == True:
# 					name[bill] = False
# 				else:
# 					name[bill] = False
# 					votes.update({person:name})	

# 			elif vote[3] == 'Not':
				
# 				person = vote[5]+' '+vote[6]
# 				if check_dictionary(votes, person) == True:
# 					name[bill] = False
# 				else:
# 					name[bill] = False
# 					votes.update({person:name})	
# 	return votes

# def  name_dictionary(list_of_names):
# 	print list_of_names
# 	names  = {}
# 	votes = {}
# 	for name in list_of_names:
# 		if name in names:
# 			pass
# 		else:
# 			names[name] =  votes

# 	return names

# def vote_dictionary(data,names):

# 	for entry in data:

# 		data_list = data[entry]
# 		bill = entry
# 		for vote in data_list:
# 			votes = {}
# 			vote = vote.replace(","," ").split()
# 			if vote[3] == 'Yea':
# 				person = str(vote[4]+' '+vote[5]) 
# 				votes[bill] = True
# 				name[person]  = votes
			
# 			elif vote[3] == 'Nay':
				
# 				person = vote[4]+' '+vote[5]
# 				votes[bill] = True
# 				name[person]  = votes

# 			elif vote[3] == 'Not':
				
# 				person = vote[5]+' '+vote[6]
# 				votes[bill] = True
# 				name[person]  = votes

# 	return names	