import os
import csv

#Setting path for csv file
file = r"C:\Users\jobel\OneDrive\Documents\UM\python-challenge\PyBank\Resources\budget_data.csv"
#Opening in read mode and storing as a CSV file
with open(file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    #Reading header row and first row
    csv_header = next(csv_reader)
    csv_first_row = next(csv_reader)

    #Variables
    months = []
    profit_loss = []
    number_of_months = 0
    net_total = 0
    P_L = 0 
    changes_P_L = 0

    P_L = int(csv_first_row[1])
    number_of_months = number_of_months + 1
    net_total = net_total + P_L
    
    for row in csv_reader:
        months.append(row[0])
        #Changes in Profit and Loss
        changes_P_L = int(row[1]) - P_L
        profit_loss.append(changes_P_L)
        P_L = int(row[1])
        #Continue to add the total number of months
        number_of_months = number_of_months + 1
        #Contunie to add for the Net total amount of Profit and Loss
        net_total = net_total + int(row[1])
        #Average of the changes
        average_change = sum(profit_loss)/len(profit_loss)
        
    #Greatest Increase
    greatest_increase = max(profit_loss)
    greatest_increase_month = months[profit_loss.index(greatest_increase)]
    #Greatest Decrease
    greatest_decrease = min(profit_loss)
    greatest_derease_month = months[profit_loss.index(greatest_decrease)]
    
#Printing budget data
print(f'Financial Analysis')
print(f'-------------------------')
print(f'Total Months: {number_of_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${str(round(average_change,2))}')
print(f"Greatest Increase in Profits: {greatest_increase_month} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {greatest_derease_month} (${str(greatest_decrease)})")
 
#Exporting a text file with the results
export = (f"Financial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {number_of_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${str(round(average_change,2))}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${str(greatest_increase)})\n"
    f"Greatest Decrease in Profits: {greatest_derease_month} (${str(greatest_decrease)})")

file_export = r"C:\Users\jobel\OneDrive\Documents\UM\python-challenge\PyBank\analysis/export_pybank.txt"
with open(file_export,"w") as textfile:
    textfile.write(export)