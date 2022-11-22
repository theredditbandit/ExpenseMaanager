import csv

# Creating a CSV FILE

fields = ["Money"]
rows = [10]
filename = "money_records.csv"

with open(filename, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerow(rows)

# Testing out a function
# with open("money_records.csv", 'r') as csvfile:
# csvreader = csv.reader(csvfile)
# for row in csvreader:
# print(row)

# Calling the data from the csv file and converting it into an integer
file = open("money_records.csv", "r")
file_data = file.read()
details = file_data.split("\n")
demo = int(details[2])


def add_money():
    global money
    file = open("money_records.csv", "r")
    file_data = file.read()
    details = file_data.split("\n")
    demo = int(details[2])
    money = int(input("How Much Would You Like To Add ? "))
    new_bal = demo + money
    print(new_bal)  # Testing if code is working or not
    u = open("money_records.csv", "r")
    update = csv.writer(u)
    bal_up = iter([new_bal])
    update.writerow(bal_up)


# Running the function
add_money()

# Overall issue I am facing is that after adding the new balance I am unable to store the data again into a csv file
# Due to this I am unable to continue the code

# Still need to do:-
# 1. Storing the new balance into the csv file in a new row
# 2. Creating a loop code for the mentioned above functionality
# 3. Refining the code
