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


def different_numbers(list_of_numbers):
    set_of_different_numbers = set()
    for element in list_of_numbers:
        set_of_different_numbers.add(element)
    return len(set_of_different_numbers)


def demo():
    total_telephone_numbers = []
    for call in calls:
        total_telephone_numbers.append(call[0])
        total_telephone_numbers.append(call[1])
    for text in texts:
        total_telephone_numbers.append(text[0])
        total_telephone_numbers.append(text[1])
    list_of_different_telephone_numbers = different_numbers(total_telephone_numbers)
    print("There are {} different telephone numbers in the records.".format(list_of_different_telephone_numbers))


demo()


# Calculate Big O:
# loop => O(n)
# add element into set => O(1)
# total = O(n * 1)
# O(n)
