# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 21:39:55 2023

@author: aosen
"""
# open file
file = open("election_data.csv")

# read the first line
category = file.readline()
categories = category.split(",")
count = 1
totalVote = 0
candidate = ""
poll = []
election = []
for line in file:
    if line != category:
        line = line.split(",")
        totalVote += 1
        candidateTuple = (candidate, count)
        if candidate != line[2].replace("\n", ""):
            count = 0
            poll.append(candidateTuple)
            candidate = line[2].replace("\n", "")
        count += 1

poll.append((candidate, count))

for i in range(1, 4):
    votes = poll[i][1]+poll[i+3][1]+poll[i+6][1]
    election.append(
        (poll[i][0], float("{:.3f}".format(votes/totalVote*100)), votes))

winner = ""
ballotCount = 0
for i in range(len(election)):
    if ballotCount < election[i][2]:
        ballotCount = election[i][2]
        winner = election[i][0]
results = ""
for i in range(len(election)):
    results = results + election[i][0] + ": " + str(election[i]
                                                    [1])+"% ("+str(election[i][2])+")\n"
analysis = "Election Results\n-------------------------\nTotal Votes: " + \
    str(totalVote)+"\n-------------------------\n"+results + \
    "-------------------------\nWinner: "+winner+"\n-------------------------"
print(analysis)
with open('PyPoll.txt', 'w') as f:
    f.write(analysis)
