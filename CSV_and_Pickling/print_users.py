import csv
 
def print_users():
    with open("users.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader: 
            print("{} {}".format(row['First Name'], row['Last Name']))


print_users()
# prints to the console:
