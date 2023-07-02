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
