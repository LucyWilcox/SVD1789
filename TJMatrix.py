from numpy import matrix, zeros
from votelist import house_votes 
from TJ_dictionary import get_data, get_votes_names

# num_members = len(house_dict)

# house_matrix = zeros(shape(num_members, num_members))


def compare_list(list1, list2):
	total_true = 0
	for entry in list1:
		if entry == True:
			total_true += 1

	true_count = 0
	for i in range(len(list1)):
		if list1[i] == True & list2[i] == True:
			true_count += 1
	percent_match = float(true_count)/total_true
	return percent_match

def to_full_list(voter, house_votes):
	voting_list = []
	for bill in house_votes:
		if bill not in voter.keys():
			voting_list.append(False)
		else:
			voting_list.append(voter[bill])
	return voting_list

def create_voter_list(house_dict):
	"""Generates a list of voters names """
	voters = []
	for key in sorted(house_dict):
		voters.append(key)
	return voters



list1 = [True, True, True, False]
list2 = [True, True, False, False]

#print compare_list(list1, list2)

house_data = get_data(house_votes)
house_dict = get_votes_names(house_data)
print house_dict

voters = create_voter_list(house_dict)
for voter in voters:
	print voter
	print house_dict[voter]
	#print to_full_list(house_dict[voter], house_votes)
