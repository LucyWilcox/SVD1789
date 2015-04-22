


from numpy import matrix, zeros, shape, set_printoptions, nan, asarray, savetxt
from votelist import house_votes, house_voters, senate_votes, senate_voters
from TJ_dictionary import get_data, get_votes_names, to_complete_dict

house_num_members = len(house_voters)
senate_num_members = len(senate_voters)

house_matrix = zeros((house_num_members, house_num_members))
senate_matrix = zeros((senate_num_members -1, senate_num_members-1))

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

def to_full_list(voter, votes):
	voting_list = []
	for bill in votes:
		if bill not in voter.keys():
			voting_list.append(False)
		else:
			voting_list.append(voter[bill])
	return voting_list

# def create_voter_list(house_dict):
# 	"""Generates a list of voters names """
# 	voters = []
# 	for key in sorted(house_dict):
# 		voters.append(key)
# 	return voters

def votes_at_i(i, voters, votes, final_dict):
	voter = voters[i]
	return to_full_list(final_dict[voter], votes)


def matrix_creation(voters, votes, final_dict):
	for i in range(len(voters) -1):
		voter1 = votes_at_i(i, voters, votes, final_dict)
		for j in range(len(voters) -1):
			voter2 = votes_at_i(j, voters, votes, final_dict)
			agreement = compare_list(voter1, voter2)
			senate_matrix[i][j] = agreement
	return senate_matrix


set_printoptions(threshold=nan)
data = get_data(senate_votes)
the_dict = get_votes_names(data, senate_voters)
final_dict = to_complete_dict(the_dict)
agreement_matrix = matrix_creation(senate_voters, senate_votes,final_dict)
print agreement_matrix
a = asarray(agreement_matrix)
savetxt("TJcsvmatrixsenate.csv", a, delimiter = ",")
#print agreement_matrix.shape
#print house_dict

