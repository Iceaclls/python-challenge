import os
import csv

number_of_votes=0


can1t=0
can2t=0
can0t=0
candidates=[]
candidate_votes={}



budget_data_csv = os.path.join("Resources", "election_data.csv")

output_file = "Analysis/output.txt"

with open('Resources/election_data.csv') as csvfile:  
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        can=(str(row["Candidate"]))
        
        number_of_votes += 1

        if can not in candidates:
            candidates.append(can)

        if can == str(candidates[0]):
            can0t += 1
        elif can == str(candidates[1]):
            can1t += 1
        elif can == str(candidates[2]):
            can2t += 1

    for row in candidates: 
        print(row) 

can0p = (can0t/number_of_votes)*100
can1p = (can1t/number_of_votes)*100
can2p = (can2t/number_of_votes)*100

can0pp = str(round(can0p, 3))
can1pp = str(round(can1p, 3))
can2pp = str(round(can2p, 3))

if can0t > can1t and can2t:
    winner=candidates[0]
if can1t > can0t and can2t:
    winner=candidates[1]
if can2t > can1t and can0t:
    winner=candidates[2]

output = f"""
Election Results
-------------------------
Total Votes: {number_of_votes}
-------------------------
{candidates[0]}: {can0pp}% ({can0t})
{candidates[1]}: {can1pp}% ({can1t})
{candidates[2]}: {can2pp}% ({can2t})
-------------------------
Winner: {winner}
-------------------------
"""

print(output)

with open(output_file, "w") as out_file:
    out_file.write(output)
    