# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 11:51:04 2021

@author: Jenkir
"""

import os

# Module for reading CSV files
import csv
from statistics import mean

total_months = 0
total_profit_loss = 0
#temp amount used to store previous month profit/loss
temp_amount = 0
#changes is a list where we will put monthly changes
changes = []

change = 0
max_change = ["", -999999]
min_change = ["", 999999]

csvpath = os.path.join('budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        total_months = total_months + 1
        total_profit_loss = total_profit_loss + int(row[1])
        change = int(row[1]) - temp_amount
        if row[0] != "Jan-2010":
            changes.append(change)
            if change > max_change[1]:
                max_change = [row[0], change]
            if change < min_change[1]:
                min_change = [row[0], change]
               
        temp_amount = int(row[1])
                
print(total_months)
print(total_profit_loss)
print(changes)
print(mean(changes))
print(max_change)
print(min_change)
    

        
