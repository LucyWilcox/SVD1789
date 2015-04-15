import csv

with open ("congress_votes_1-1_h32.csv", 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print " ".join(row)