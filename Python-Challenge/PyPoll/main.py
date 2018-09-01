#Dependencies
import os
import csv

# Set input file path
csvpath = os.path.join("Resources","election_data.csv")

#Creates dictionary to be used for candidate name and vote count.
candidates_votes = {}

#Sets variable, total votes, to zero for count.
total_votes = 0

#gets data file
with open(csvpath) as csvfile:
    csvread = csv.reader(csvfile)

    #skips header line
    next(csvread, None)

    #creates dictionary from file using column 3 as keys, using each name only once.
    #counts votes for each candidate as entries
    #keeps a total vote count by counting up 1 for each loop (# of rows w/o header)
    for row in csvread:
        total_votes += 1
        if row[2] in candidates_votes.keys():
            candidates_votes[row[2]] = candidates_votes[row[2]] + 1
        else:
            candidates_votes[row[2]] = 1
 
#create empty list for candidates and his/her vote count
candidates = []
votes = []

#takes dictionary keys and values and, respectively, dumps them into the lists, 
# candidates and votes
for key, value in candidates_votes.items():
    candidates.append(key)
    votes.append(value)

#vote percentage
vote_percent = []
for n in votes:
    vote_percent.append(round(n/total_votes*100, 1))

# zips candidates, votes, vote_percent into tuples
clean_data = list(zip(candidates, votes, vote_percent))

#creates winner_list to put winners (even if there is a tie)
winner_list = []

for name in clean_data:
    if max(votes) == name[1]:
        winner_list.append(name[0])

# makes winner_list a str with the first entry
winner = winner_list[0]

#prints to file
file_to_output = os.path.join("Resources/election_results.txt")

with open(file_to_output, 'w') as txt_file:
    txt_file.write('Election Results')
    txt_file.write('\n')
    txt_file.write('----------------------------')
    txt_file.write('\n')
    txt_file.write('Total Votes:'+ str(total_votes))                 
    txt_file.write('\n---------------------------')
    txt_file.write('\n')
    
    for entry in clean_data:
        txt_file.write(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txt_file.write('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open(file_to_output, 'r') as readfile:
    print(readfile.read())
