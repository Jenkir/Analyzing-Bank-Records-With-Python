# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import os
import csv


file = os.path.join("Resources","budget_data.csv") 

#create empty lists for csv values
month_count = []
profit = []
change = []


with open('budget_data.csv', 'r') as csvfile:

 # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header and append to lists
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change.append(profit[i+1]-profit[i])
        
#calc max and min from the lists made
increase = max(change)
decrease = min(change)

#index
month_increase = change.index(max(change))+1
month_decrease = change.index(min(change))+1

    
#print analysis and export text file
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change)/len(change),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")      
               

output = os.path.join(".", 'output.txt')
with open(output, "w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(month_count)}")
    new.write("\n")
    new.write(f"Total: ${sum(profit)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(change)/len(change),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")

