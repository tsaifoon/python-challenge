
import os
import csv
from datetime import datetime

csvPath = os.path.join(".","Resources","budget_data.csv")

month = []
proLoss = []

with open(csvPath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    #skip first title line.
    next(csvreader)
    for row in csvreader:
        month.append(row[0])
        proLoss.append(row[1])


#The total number of months included in the dataset - take last value in list minus first to find total time.
newFirstDate = datetime.strptime(month[0], '%b-%Y')
newLastDate = datetime.strptime(month[len(month)-1], '%b-%Y')
totalMonth = 0
#needs conversion to numeric format
#**output not quite right -- how to convert the "day" to "months" 
totalMonth = (newLastDate - newFirstDate)/365.25 * 12
print(f"Financial Analysis")
print(f"-----------------------------")
print(f"Total Months:{totalMonth}")


#The net total amount of "Profit/Losses" over the entire period
totChange = 0
for x in proLoss:
    totChange += int(x)
print(f"Total: ${totChange}")


#The average of the changes in "Profit/Losses" over the entire period
avgChange = []
#first change is zero
initial = int(proLoss[0])
for x in proLoss:
    change = 0
    #subtract new from previous value for change
    change = int(x) - initial
        #Test - print(f"{change} {x}")
    #append to new array
    avgChange.append(change)
    initial = int(x)
#initialize average value
totAvg = 0
avgChange.pop(0)
for x in avgChange:
    totAvg += int(x)
avgValue = totAvg / len(avgChange)   
print(f"Average Change: ${avgValue}")


#The greatest increase in profits (date and amount) over the entire period
gInc = 0
gIncDate = ""
gIncIndex = 0
for x in avgChange:
    if(x > gInc):
        gInc = x
        gIncIndex = avgChange.index(x)
        # QA test - print(f"{gIncIndex}")
        gIncDate = month[gIncIndex]
print(f"Greatest Increase in Profits: {gIncDate} (${gInc})")

#The greatest decrease in losses (date and amount) over the entire period
gDec = 0
gDecDate = ""
gDecIndex = 0
for x in avgChange:
    if(x < gDec):
        gDec = x
        gDecIndex = avgChange.index(x)
        # QA test - print(f"{gDecIndex}")
        gDecDate = month[gDecIndex]
print(f"Greatest Decrease in Profits: {gDecDate} (${gDec})")

tupOne = zip(month,proLoss,avgChange)



#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
output_file = os.path.join("pyBankOutput.csv")
with open(output_file,"w",newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Date","Profit/Losses","Average Change"])
    writer.writerows(tupOne)
    writer.writerow("\n")
    writer.writerow(["Financial Analysis"])
    writer.writerow(["--------------------"])
    writer.writerow(["Total Months: ", totalMonth])
    writer.writerow(["Total: ", totChange])
    writer.writerow(["Average Change: ", avgValue])
    writer.writerow(["Greatest Increase in Profits: ", gInc])
    writer.writerow(["Greatest Decrease in Profits: ", gDec])
