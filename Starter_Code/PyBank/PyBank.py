import csv


import os

input_path = os.path.join("Resources", "budget_data.csv")

with open(input_path) as file:
    reader = csv.reader(file)

    header = next(reader)

    total_months = 0  
    total_revenue = 0

    changes = []
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_month =''
    greatest_decrease_month =''
    

    for i, row in enumerate(reader):

        total_months += 1
        total_revenue += int(row[1])

        if i == 0: 
            previous_profitlost = int(row[1])

        else:
            change = int(row[1]) - previous_profitlost
            changes.append(change)
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]
            previous_profitlost = int(row[1])
        
print(total_months)
print(total_revenue)

change_sum = 0
for c in changes:
    change_sum += c

average_change = change_sum/len(changes)
print(average_change)

 

print(greatest_increase, greatest_increase_month)
print(greatest_decrease, greatest_decrease_month)     

print(f"total month {total_months}")
print(f"total revenue {total_revenue}")
print(f"average change{average_change}")
print(f"greatest increase in profit {greatest_increase_month}")
print(f"greatest decrease in profit  {greatest_decrease_month}")