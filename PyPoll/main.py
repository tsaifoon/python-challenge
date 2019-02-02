
import os
import csv

csvPath = os.path.join('.','Resources','election_data.csv')

voterID = []
county = []
candidate = []

with open(csvPath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    #skip first title line.
    next(csvreader)
    for row in csvreader:
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#The total number of votes cast
totalVotes = 0
for voter in voterID:
    totalVotes += 1

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {totalVotes}")