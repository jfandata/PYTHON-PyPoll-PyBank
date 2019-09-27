# PyBank and PyPoll
This project is part of the Data Analytics and Visualization Certification at Washington University in St. Louis.  Other projects can be found at the [main GitHub repo](https://github.com/jfandata).

#### -- Project Status: [Completed]

## Project Intro/Objective
The objective of the project is to use Python scripting skills to analyze real world situations. PyBank analyzes company financial records and financial performance over time. PyPoll count and analyze voting data to determine the winner of the election. 

### Methods Used
* Python scripts

### Technologies
* Python

## Project Description
PyBank: create a Python script that analyzes the records to calculate each of the following:
- The total number of months included in the dataset
- The total net amount of "Profit/Losses" over the entire period
- The average change in "Profit/Losses" between months over the entire period
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in losses (date and amount) over the entire period

PyPoll: create a Python script that analyzes the votes and calculates each of the following:
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote.

## Needs of this Project

- data processing/cleaning
- data exploration
- python script

## Contents of Project Repository

1. Raw data for PyBank is kept within this [repo](https://github.com/jfandata/PYTHON-PyPoll-PyBank/tree/master/PyBank/Resources).

2. Raw data for PyPoll is kept within this [repo](https://github.com/jfandata/PYTHON-PyPoll-PyBank/tree/master/PyPoll/Resources).

2. Data processing/transformation scripts (file main.py) for PyBank are being kept [here](https://github.com/jfandata/PYTHON-PyPoll-PyBank/blob/master/PyBank/main.py) and PyPoll are kept [here](https://github.com/jfandata/PYTHON-PyPoll-PyBank/blob/master/PyPoll/main.py)

3. Results for PyBank are being kept [here](https://github.com/jfandata/PYTHON-PyPoll-PyBank/blob/master/PyBank/Results.txt) and PyPoll are kept [here](https://github.com/jfandata/PYTHON-PyPoll-PyBank/blob/master/PyPoll/Results.txt)

## Key Takeaways

1. Import dependencies.

```python
import os
import csv
```

2. Create a path to raw data, read and open csv with headers.

```python
csvpath = os.path.join("Resources/budget_data.csv")

with open (csvpath, newline="") as csvfile:
    csv_reader =csv.reader(csvfile, delimiter=",")
    csv_headers = next(csv_reader, None)
```

3. Python lists are written with [] square brackets. Create lists to store data.

```python
months = []
profit = []
```

4. Write a for loop to go through csv data and append to lists created in #3. 

```python
for row in csv_reader:
    months.append(row[1])
    profit.append(int(row[1]))
```

5. Apply min and max functions and print results.

```python
max_change = max(change)
print (f"${max_change}")

min_change = min(change)
print (f"${min_change}")
```

6. Export results.

```python
exportpath = ("Results.txt")
with open(exportpath, "w") as textfile:
    textfile.write(f"Total Months: {total_months}")
    textfile.write(f"Total: ${revenues}")
    textfile.write(f"Average Change: ${round((average_month),2)}")
    textfile.write(f"Greatest Increase in Revenues: ${max_change}")
    textfile.write(f"Greasest Decrease in Revenues:  ${min_change}")
```


