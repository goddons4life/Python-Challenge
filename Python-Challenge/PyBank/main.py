#Dependencies
import csv
import os

# Path to the resources folder
csv.path = os.path.join("Resources","budget_data.csv")

#lists for month and profit/loss data
months = []
profit_loss = []

#read csv 
with open(csv.path, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        profit_loss.append(int(row[1]))

#To find total month
total_months = len(months)

#create variables for greatest increase, decrease

greatest_increase = profit_loss[0]
greatest_decrease = profit_loss[0]
total_profit_loss = 0

#Loop through all the rows of data we collect and add the total

for p in range(len(profit_loss)):
    if profit_loss[p] >= greatest_increase:
        greatest_increase = profit_loss[p]
        great_increase_month = months[p]
    elif profit_loss[p] <= greatest_decrease:
        greatest_decrease = profit_loss[p]
        great_decrease_month = months[p]
    total_profit_loss += profit_loss[p]

#calculate average_change
average_change = round(total_profit_loss/total_months, 2)

#output file path
file_to_output = os.path.join("Resources/budget_analysis.txt")

# Show output
with open(file_to_output, 'w') as txt_file:
    txt_file.write('Financial Analysis\n')
    txt_file.write('----------------------------' + '\n')
    txt_file.write('Total Months: ' + str(total_months) + '\n')
    txt_file.write('Total Profit_loss: $' + str(total_profit_loss) + '\n')
    txt_file.write('Average Profit_loss Change: $' + str(average_change) + '\n')
    txt_file.write('Greatest Increase in Profit_Loss: ' + great_increase_month + ' ($' + str(greatest_increase) + ')'+ '\n')
    txt_file.write('Greatest Decrease in Profit_Loss: ' + great_decrease_month + ' ($' + str(greatest_decrease) + ')')

#opens output file in row mode and prints to terminal
with open(file_to_output, 'r') as readfile:
    print(readfile.read())
