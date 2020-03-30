"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def different_telephone_numbers(input_list):
    different_list = []
    for element in input_list:
        if element not in different_list:
            different_list.append(element)
    return len(different_list)


def demo():
    total_telephone_numbers = []
    for i in range(len(calls)):
        total_telephone_numbers.append(calls[i][0])
        total_telephone_numbers.append(calls[i][1])
    for i in range(len(texts)):
        total_telephone_numbers.append(texts[i][0])
        total_telephone_numbers.append(texts[i][1])
    count = different_telephone_numbers(total_telephone_numbers)
    print("There are {} different telephone numbers in the records.".format(count))


demo()


# Calculate Big O:
# loop => O(n)
# check element in different_list => O(m)
# append => O(1)
# total = O(n * m + 1)
# O(n^2)
