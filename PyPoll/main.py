import os
import csv

number_of_votes=0


can1t=0
can2t=0
can0t=0
candidates=[]
candidate_votes={}

#Converts the CSV file
budget_data_csv = os.path.join("Resources", "election_data.csv")
output_file = "Analysis/output.txt"
with open('Resources/election_data.csv') as csvfile:  
    csvreader = csv.DictReader(csvfile)
    
    for row in csvreader:
        can=(str(row["Candidate"]))
#Counts the number of rows (votes)
        number_of_votes += 1

#Seperates the unique values in the candidates column
        if can not in candidates:
            candidates.append(can)

#Counts the total number of votes each candidate has
        if can == str(candidates[0]):
            can0t += 1
        elif can == str(candidates[1]):
            can1t += 1
        elif can == str(candidates[2]):
            can2t += 1

    #displays the candidates
    for row in candidates: 
        print(row) 

#Percentage of votes each candidate had
can0p = (can0t/number_of_votes)*100
can1p = (can1t/number_of_votes)*100
can2p = (can2t/number_of_votes)*100

#Convertes the percentage to 3 decimals
can0pp = str(round(can0p, 3))
can1pp = str(round(can1p, 3))
can2pp = str(round(can2p, 3))

#Decides which candidate has won
if can0t > can1t and can2t:
    winner=candidates[0]
if can1t > can0t and can2t:
    winner=candidates[1]
if can2t > can1t and can0t:
    winner=candidates[2]

#Makes output file and display
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
    
