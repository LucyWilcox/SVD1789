


from numpy import matrix, zeros, shape, set_printoptions, nan, asarray, savetxt
from votelist import house_votes, house_voters
from TJ_dictionary import get_data, get_votes_names, to_complete_dict

num_members = len(house_voters)

house_matrix = zeros((num_members, num_members))

def compare_list(list1, list2):
	total_true = 0
	for entry in list1:
		if entry == True:
			total_true += 1
	if total_true == 0:
		return 0
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
			print t
		else:
			voting_list.append(voter[bill])
	return voting_list

# def create_voter_list(house_dict):
# 	"""Generates a list of voters names """
# 	voters = []
# 	for key in sorted(house_dict):
# 		voters.append(key)
# 	return voters

def votes_at_i(i, house_voters, house_votes, final_house_dict):
	voter = house_voters[i]
	return to_full_list(final_house_dict[voter], house_votes)


def matrix_creation(house_voters, house_votes,final_house_dict):
	for i in range(len(house_voters) -1):
		voter1 = votes_at_i(i, house_voters, house_votes, final_house_dict)
		for j in range(len(house_voters) -1):
			voter2 = votes_at_i(j, house_voters, house_votes, final_house_dict)
			agreement = compare_list(voter1, voter2)
			house_matrix[i][j] = agreement
	return house_matrix

list1 = [True, True, True, False]
list2 = [True, True, False, False]

#print compare_list(list1, list2)
set_printoptions(threshold=nan)
house_data = get_data(house_votes)
house_dict = get_votes_names(house_data, house_voters)
final_house_dict = to_complete_dict(house_dict)
agreement_matrix = matrix_creation(house_voters, house_votes,final_house_dict)
print agreement_matrix
a = asarray(agreement_matrix)
savetxt("TJcsvmatrix.csv", a, delimiter = ",")
#print agreement_matrix.shape
#print house_dict

