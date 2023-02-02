import csv
import sys

# Helper function for parsing the times
# Takes a list and a delimiter to split the last element in the list
# Returns the list with the split items added to it

def split_and_remove(in_list, char):
    split_item = in_list[len(in_list) - 1]
    new_list = split_item.split(char)
    del in_list[len(in_list) - 1]
    in_list += new_list
    return in_list

# Helper function for converting the time of each transaction into a format
# that can be sorted: This works by creating a list of integers where the first integer is
# the year, the second is the month, the third is the day, etc.

def parse_time(timestamp):
    timestamp_list = timestamp.split('-')
    timestamp_list = split_and_remove(timestamp_list, 'T')
    timestamp_list = split_and_remove(timestamp_list, ':')
    timestamp_list = split_and_remove(timestamp_list, 'Z')
    del timestamp_list[len(timestamp_list) - 1]
    return timestamp_list

# Returns a list of entries from the CSV. Excludes the first line (indices)
# of the CSV, since it is assumed that they will be the same every time.

def get_csv_from_file(csv_input):
    with open(csv_input) as file:
        read_csv = csv.reader(file, delimiter=',')
        master_list = []
        first_row = True
        for row in read_csv:
            if not first_row:
                master_list.append(row)
            else:
                first_row = False
    return master_list
        
# Converts the list of integers from parse_time into a numerical
# value that can be compared. 
        
def sort_by_time(a):
    total_key = 0
    for i in range(len(a[2])):
        total_key += int(a[2][i])*(100**(-i))
    return total_key

# Here's how you look at it:
# You start out with (input) number of points. 
# When a company asks for x number of points (positive integer), x points
# are deducted from your account. 
# When x is a negative integer, that many points are put back into your account.
# If x > number of points you have, the number of points you have is deducted, your
# point total goes to 0, the remainder is the company's balance.

# What happens if a company has a pending balance and you gain more points, 
# putting your total above 0? The way I see it, those points should be used
# to fulfill the earliest request for more points that hasn't been completely
# filled. 

# The reason why I analyzed all of the deposits before all of the withdrawals
# is because of two points:
# 1) The order in which each transaction is processed does not matter,
# all that matters is that the end result is correct.
# 2) Whenever a new deposit comes in, if there is still a pending balance,
# this deposit is used to pay off the oldest possible balance.

if __name__ == "__main__":
    starting_total = int(sys.argv[1]) # This is changed based on user input
    # This assumes only one number is put into the command line
    # as well as assuming that it is an integer
    csv_to_list = get_csv_from_file('samplebackend.csv')
    # This is assuming that the file being put in will always be named
    # 'samplebackend.csv'
    for i in range(len(csv_to_list)):
        csv_to_list[i][2] = parse_time(csv_to_list[i][2])
    deposits = [x for x in csv_to_list if int(x[1]) < 0]
    withdrawals = [x for x in csv_to_list if int(x[1]) > 0]
    # I do not need to handle the case where x[1] == 0, since that does nothing
    deposits.sort(key=sort_by_time)
    withdrawals.sort(key=sort_by_time)
    for deposit in deposits:
        starting_total -= int(deposit[1]) # Value is being added since I am subtracting a negative number
    company_balances = {}
    for withdrawal in withdrawals:
        if int(withdrawal[1]) >= starting_total:
            current_withdrawal = int(withdrawal[1]) - starting_total
            starting_total = 0
            company_balances[withdrawal[0]] = current_withdrawal
        else:
            starting_total -= int(withdrawal[1])
            company_balances[withdrawal[0]] = 0
    # The balances you are looking for are printed out.
    print(company_balances)
