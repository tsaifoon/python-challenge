
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

print(f"Election Results")
print(f"-------------------------")

#The total number of votes cast
totalVotes = 0
for voter in voterID:
    totalVotes += 1

print(f"Total Votes: {totalVotes}")
print(f"-------------------------")

#A complete list of candidates who received votes
#create a new array for unique candidates
uniqCand = []
for people in candidate:
    #compare long list with not long list
        if(people not in uniqCand):
            uniqCand.append(people)

#The percentage of votes each candidate won
comboList = []
for unique in uniqCand:
    count = 0
    for people in candidate:            
        if(people == unique):
            count += 1
    comboList.append( [unique,(count/totalVotes * 100),count] )
    print(f"{unique}: {round(count/totalVotes * 100,3)}% ({count})")        

print(f"{comboList[0][1]}")
winName = ""
winner = 0
for x in comboList:
   if(comboList[comboList.index(x)][1] > winner):
        winner = comboList[comboList.index(x)][1]
        winName = comboList[comboList.index(x)][0]

print(f"-------------------------")
print(f"Winner: {winName}")
print(f"-------------------------")
#The total number of votes each candidate won

#The winner of the election based on popular vote.

