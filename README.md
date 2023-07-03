# python-challenge
Peer colloboration with Ryan Himes, Jennifer Grubb, and Juliet Hamilton. 

PyBank:
import os
import csv
# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")

# Create Lists
Months =[]
Profit_loss = []
Increase_decrease = []

# Read file and creat list from csv file
with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        Months.append(row[0])
        Profit_loss.append(row[1])

# convert profit to intenger
    Profit_loss = [int(i) for i in Profit_loss]

# Find the greatest increase in profits and greatest decrease in profits
for i in range(len(Profit_loss) - 1):
    Increase_decrease.append(Profit_loss[i + 1] - Profit_loss[i])
max_increase_value = max(Increase_decrease)
max_decrease_value = min(Increase_decrease)
max_increase_index = Increase_decrease.index(max_increase_value)
max_decrease_index = Increase_decrease.index(max_decrease_value)
max_increase_month = Months[max_increase_index + 1]
max_decrease_month = Months[max_decrease_index + 1]

# Calculate total months, total profit and average of increase_decrease in Profit
Total_Months = len(Months)
Total_Profit = sum(Profit_loss)
Avg_Difference = round((Profit_loss[-1] - Profit_loss[0]) / ((Total_Months)- 1),2)

# Print to Terminal
print("")
print(f'Financial Analysis')
print("")
print(f'-------------------------')
print("")
print(f'Total Months: {Total_Months}')
print("")
print(f'Total:  ${Total_Profit}')
print("")
print(f'Average Change: ${Avg_Difference}')
print("")
print(f"Greatest Increase in Profits: {max_increase_month} (${(str(max_increase_value))})")
print("")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${(str(max_decrease_value))})")

# Set output for text file
output = (f'\n'
f'Financial Analysis\n'
f'\n'
f'-------------------------\n'
f'\n'
f'Total Months: {Total_Months}\n'
f'\n'
f'Total:  ${Total_Profit}\n'
f'\n'
f'Average Change: ${Avg_Difference}\n'
f'\n'
f"Greatest Increase in Profits: {max_increase_month} (${(str(max_increase_value))})\n"
f'\n'
f"Greatest Decrease in Profits: {max_decrease_month} (${(str(max_decrease_value))})\n")

# Set variable for output file
output_file = os.path.join("analysis","budget_final.txt")

#  Open and Write to the output text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)

PyPoll: 
import os
import csv
# Path to collect data from the Resources folder
election_csv = os.path.join("Resources", "election_data.csv")
# Create Lists
Candidate = []
Person = []
Vote_Count = []
Vote_Percentage = []
Candidates = {}
# Read in the CSV file
with open(election_csv) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    # count total votes and votes for each candidate, Loop through the data
    for row in csvreader:
        Candidate.append(row[2])
        Total_Votes = len(Candidate)
        person = row[2]
        if person not in Candidates:
            Candidates[person] = 1
        else:
            Candidates[person] += 1
# Appending Lists with candidate name, vote count and voter % based on loop above
    for person, vote_count in Candidates.items():
        Person.append(person)
        Vote_Count.append(vote_count)
        Percentage_Vote = round((vote_count / Total_Votes) *100,3)
        Vote_Percentage.append(Percentage_Vote)
# Find max votes in voter count to determine winnner
Winning_Candidate = max(Candidates, key=Candidates.get)

# Print election results to terminal
print("")
print(f'Election Results')
print("")
print(f'-------------------------')
print("")
print (f'Total Votes: {Total_Votes}')
print("")
print(f'-------------------------')
print(f'{Person[0]}: {Vote_Percentage[0]}% ({Vote_Count[0]})')
print("")
print(f'{Person[1]}: {Vote_Percentage[1]}% ({Vote_Count[1]})')
print("")
print(f'{Person[2]}: {Vote_Percentage[2]}% ({Vote_Count[2]})')
print(f'-------------------------')
print("")
print(f'Winner: {Winning_Candidate}')
print("")

# Set output for text file
output = (f'\n'
f'Election Results\n'
f'\n'
f'-------------------------\n'
f'\n'
f'Total Votes: {Total_Votes}\n'
f'\n'
f'-------------------------\n'
f'{Person[0]}: {Vote_Percentage[0]}% ({Vote_Count[0]})\n'
f'\n'
f'{Person[1]}: {Vote_Percentage[1]}% ({Vote_Count[1]})\n'
f'\n'
f'{Person[2]}: {Vote_Percentage[2]}% ({Vote_Count[2]})\n'
f'-------------------------\n'
f'\n'
f'Winner: {Winning_Candidate}\n'
f'\n')
# Set variable for output file
output_file = os.path.join("analysis","election_final.txt")

#  Open and Write to the output text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)
