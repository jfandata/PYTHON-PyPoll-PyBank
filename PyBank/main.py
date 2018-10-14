import os
import csv

csvpath = os.path.join("Resources/budget_data.csv")

with open (csvpath, newline="") as csvfile:
    csv_reader =csv.reader(csvfile, delimiter=",")
    csv_headers = next(csv_reader, None)

#with open (csvpath, 'r') as csv_reader:
#    lines = csv_reader.read()


# count the months
# 1. create lists to store months and profitLoss
    months = []
    profit = []

    for row in csv_reader:
        months.append(row[1])
        profit.append(int(row[1]))

    total_months = len(months)
    print (f"Total Months: {total_months}")

# add the profit/Loss to get revenues
    revenues = 0
    i = 1
    for i in range(total_months):
        revenues = revenues + int(profit[i])
    print (f"Total: ${revenues}")

# find the average change per month
# 1. find change in profit/loss per month
    change = []
    j = 0
    k = 0

    for j in range (1, total_months):
        if j == 0:
            change.append(0)
        else:
            change.append(int(profit[j])-int(profit[k]))
            k += 1
    #print (change)
# 2. sum the monthly changes and divide by total_months
    average_month = ((sum(change))/(len(change)))
    print (f"Average Change: ${round((average_month),2)}")

# greatest increase in profits
    max_change = max(change)
    print (f"${max_change}")
# greatest decrease in profits
    min_change = min(change)
    print (f"${min_change}")

    
