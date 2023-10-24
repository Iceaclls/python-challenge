import os
import csv

sum=0
row_number=0
profit_change=0
previouse_profit=0
total_change=0
change=0
average=0
decrease = ["", 9999999]
increase = ["", 0]
pl1=[]
month_counter=0

#Converting the CSV file
budget_data_csv = os.path.join("Resources", "budget_data.csv")
output_file = "Analysis/output.txt"
with open(budget_data_csv) as csvfile:  
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:

        pl=(int(row["Profit/Losses"]))

        # Counts the number of rows in the dataset        
        row_number += 1

        # Takes the sum of the profit/losses        
        sum += pl

        # Calculates the average difference in profit/losses        
        if previouse_profit != 0:
            change=pl - previouse_profit
            month_counter += 1
            total_change=total_change + change
        
        previouse_profit=pl

        # Finds the max value and returns the date
        if change > increase[1]:
            increase[1]= change
            increase[0] = row['Date']

        # Finds the min value and returns the date
        if change<decrease[1]:
            decrease[1]= change
            decrease[0] = row['Date']

#Makes output txt file and display        
output = f"""
Financial Analysis
----------------------------
Total Months: {row_number}
Total: ${sum:,}
Average Change: ${total_change/month_counter:.2f}
Greatest Increase in Profits: {increase[0]} (${increase[1]:,})
Greatest Decrease in Profits: {decrease[0]} (${decrease[1]:,})
"""

print(output)

with open(output_file, "w") as out_file:
    out_file.write(output)

    
    
    
