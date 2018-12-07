# pull in csv file
import os
import csv

csvpath = os.path.join('poll_data.csv')

#format the data from csv into an array
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    data = []
    messages = []
    line = "________________________________"
    khan = []
    correy = []
    li = []
    otooley = []

#dump all the data into an empty list and get a count of all the votes    
    for row in csvreader:
        data.append(row)
    
    messages.append("Election Results")
    messages.append(line)
    messages.append(f"Total Votes: {len(data)}")
    messages.append(line)

#put candidate votes into their own list
    for i in range(len(data)):
        if data[i][2] == "Khan":
            khan.append(data[i])
        elif data[i][2] == "Correy":
            correy.append(data[i])
        elif data[i][2] == "Li":
            li.append(data[i])
        else: 
            otooley.append(data[i])
    
#display the % and number of votes for each candidate
    messages.append(f"Khan: {int(100 * len(khan)/len(data))}% {len(khan)}")
    messages.append(f"Correy: {int(100 * len(correy)/len(data))}% {len(correy)}")
    messages.append(f"Li: {int(100 * len(li)/len(data))}% {len(li)}")
    messages.append(f"O'Tooley: {int(100 * len(otooley)/len(data))}% {len(otooley)}")
    messages.append(line)

#calculate the winner
    totals = []
    counts = {
        "Khan" : len(khan),
        "Correy" : len(correy),
        "Li" : len(li),
        "O'Tooley" : len(otooley)
    }
    for count in counts:
        totals.append(counts[count])
        if counts[count] == max(totals):
            messages.append(f"Winner: {count}")

    #print and output to text file
    for message in messages:
        f = open('results.txt','a')
        f.write(message + '\n')
        print(message)
