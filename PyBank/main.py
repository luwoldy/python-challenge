# pull in csv file
import os
import csv

csvpath = os.path.join('budget_data.csv')

#format the data from csv into an array
with open(csvpath, newline = '') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',')
      csv_header = next(csvreader)
      data = []
      total = []
      messages = []
      
      
      for row in csvreader:
            data.append(row)
            # loop through and add each profit/loss to a count
            total.append(int(row[1]))
            #track change month to month

# get the length of the list
      messages.append(f"There are {len(data)} months on record")
      messages.append(f"The total net profit/loss for the period is ${sum(total)}")

# create a new array to track change from month to month
      change = []
      amount = 0
      for i in range(1,len(data)):
# coninuted: calculate the average of the values in the new array
           amount = total[i] - total[i -1]
           change.append(amount)
           amount = 0 
      messages.append(f"Average change:{round(sum(change) / len(change))}")
      
      

# use min and max functions to find lowest and highest numbers    
      for i in range(len(change)):
            if change[i] == min(change):
                  minMonth = i
      messages.append(f"Greatest decrease in profits: ${min(change)} {data[minMonth + 1][0]}")

      for i in range(len(change)):
            if change[i] == max(change):
                  maxMonth = i
      messages.append(f"Greatest increase in profits: ${max(change)} {data[maxMonth + 1][0]}")

      for message in messages:

            f = open('answers.txt','a')
            f.write(message + '\n')
            print(message)
            


            
            

            




