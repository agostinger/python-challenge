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
