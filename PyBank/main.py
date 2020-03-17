import os
import csv

#create file with format:
'''
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
'''

csv_path = os.path.join("..","Resources","budget_data.csv")
with open(csv_path,'r') as csv_file:
    txt_path = os.path.join("..","Resources","final_bank_text.txt")
    csv_reader = csv.reader(csv_file, delimiter = ',')
    header = next(csv_reader)
    with open (txt_path,'w') as txt_file:
        totalMonths = 0 #The total number of months included in the dataset
        totalOfTransactions = 0 #The net total amount of "Profit/Losses" over the entire period
        averageProfitLoss = 0 #The average of the changes in "Profit/Losses" over the entire period
        greatestGain = 0 #The greatest increase in profits (date and amount) over the entire period
        monthOfGain = ""
        greatestLoss = 0 #The greatest decrease in losses (date and amount) over the entire period
        monthOfLoss = ""
        for row in csv_reader:
            monthYear = str(row[0])
            profitLoss = float(row[1])
            totalMonths += 1
            totalOfTransactions += profitLoss
            if profitLoss > greatestGain:
                greatestGain = profitLoss
                monthOfGain = monthYear
            elif profitLoss < greatestLoss:
                greatestLoss = profitLoss
                monthOfLoss = monthYear
        averageProfitLoss = totalOfTransactions / totalMonths
        #now to write the values into the text file
        txt_file.write("Financial Analysis\n----------------------------")
        txt_file.write(f"Total Months: {totalMonths}\nTotal: ${totalOfTransactions}")
        txt_file.write(f"Average Change: ${averageProfitLoss}")
        txt_file.write(f"Greatest Increase in Profits: {monthOfGain} {greatestGain}")
        txt_file.write(f"Greatest Decrease in Profits: {monthOfLoss} {greatestLoss}\n")
        #now, finally, print to terminal
        print("Financial Analysis\n----------------------------\n")
        print(f"Total Months: {totalMonths}\nTotal: ${totalOfTransactions}")
        print(f"Average Change: ${averageProfitLoss}")
        print(f"Greatest Increase in Profits: {monthOfGain} {greatestGain}")
        print(f"Greatest Decrease in Profits: {monthOfLoss} {greatestLoss}\n")