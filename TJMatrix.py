from numpy import matrix, zeros

house_dict = {}
num_members = len(house_dict)

house_matrix = zeros(shape(num_members, num_members))

for key in house_dict:
	bills = house_dict[key]
	print bills
	for key2 in bills:
		print bills[key2]


