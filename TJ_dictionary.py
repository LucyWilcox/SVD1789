import csv
from votelist import house_votes, senate_votes, house_voters, senate_voters


def get_votes_names(data, voters):
	full_dict = dict.fromkeys(voters)
	for bill in data:
		for vote in data[bill]:
			vote = vote.replace(","," ").split()
			if vote[2] == 'Yea':
				person = str(vote[3]+' '+vote[4])
				if full_dict[person] == None:
					full_dict[person] = [(bill, True)]
				else:
					full_dict[person].append((bill, True))
			
			elif vote[2] == 'Nay':
				
				person = vote[3]+' '+vote[4]
				if full_dict[person] == None:
					full_dict[person] = [(bill, False)]
				else:
					full_dict[person].append((bill, False))

			elif vote[2] == 'Not':
				
				person = vote[4]+' '+vote[5]
				if full_dict[person] == None:
					full_dict[person] = [(bill, False)]
				else:
					full_dict[person].append((bill, False))

	return full_dict


def to_complete_dict(the_dict):
	for key, value in the_dict.iteritems():
		the_dict[key] = dict(value)

	return the_dict


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


if __name__ == '__main__':
	votes = senate_votes
	voters  = senate_voters
	data = get_data(votes)
	the_dict = get_votes_names(data, voters)
	final_dict = to_complete_dict(the_dict)
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