import os
import csv

#Setting path for csv file
file = r"C:\Users\jobel\OneDrive\Documents\UM\python-challenge\PyPoll\Resources\election_data.csv"
#Opening in read mode and storing as a CSV file
with open(file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    #Reading header row and first row
    csv_header = next(csv_reader)
    file_info = list(csv_reader)
    count = len(file_info)
    
    #Variables
    names_of_candidates = []
    count_of_candidates = []
    candidates_votes = []
    percent_candidates_votes = []
 
    #List of candidates
    for x in range (0,count):
        names = file_info[x][2]
        count_of_candidates.append(names)
        if names not in names_of_candidates:
            names_of_candidates.append(names)
    list_of_candidates = len(names_of_candidates)
    
  #Total number of votes cast
    for i in range (0,list_of_candidates):
        votes = names_of_candidates[i]
        candidates_votes.append(count_of_candidates.count(votes))
        percent_for_votes = candidates_votes[i]/count
        percent_candidates_votes.append(percent_for_votes)

    #Winner of the election based on popular vote.
    final_winner = candidates_votes.index(max(candidates_votes))

# Printing election data
print("Election Results") 
print("-------------------------")
print(f"Total Votes: {count}")
print("-------------------------")
for j in range (0,list_of_candidates): 
    print(f"{names_of_candidates[j]}: {percent_candidates_votes[j]:.3%} ({candidates_votes[j]})")
print("-------------------------")
print(f"Winner: {names_of_candidates[final_winner]}")
print("-------------------------")

#Exporting a text file with the results
file1 = open("export_PyPoll.txt","a")
print("Election Results", file=file1)
print("-------------------------", file=file1)
print(f"Total Votes: {count}", file=file1)
print("-------------------------", file=file1)
for j in range (0,list_of_candidates): 
    print(f"{names_of_candidates[j]}: {percent_candidates_votes[j]:.3%} ({candidates_votes[j]})", file=file1)
print("-------------------------", file=file1)
print(f"Winner: {names_of_candidates[final_winner]}", file=file1)
print("-------------------------", file=file1)
file1.close()