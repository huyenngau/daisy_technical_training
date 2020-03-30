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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def call_numbers(call_list):
    set_of_caller_numbers = set()
    set_of_receiver_numbers = set()
    for call in call_list:
        set_of_caller_numbers.add(call[0])
        set_of_receiver_numbers.add(call[1])
    return set_of_caller_numbers, set_of_receiver_numbers


def text_numbers(text_list):
    set_of_sender_text_numbers = set()
    set_of_receiver_text_numbers = set()
    for text in text_list:
        set_of_sender_text_numbers.add(text[0])
        set_of_receiver_text_numbers.add(text[1])
    return set_of_sender_text_numbers, set_of_receiver_text_numbers


def get_telemarketer_numbers(call_list, text_list):
    telemarketer_numbers = set()

    set_of_caller_numbers, set_of_receiver_numbers = call_numbers(call_list)
    set_of_sender_text_numbers, set_of_receiver_text_numbers = text_numbers(text_list)

    for telephone_number in set_of_caller_numbers:
        if telephone_number not in set_of_receiver_numbers \
           and telephone_number not in set_of_sender_text_numbers \
           and telephone_number not in set_of_receiver_text_numbers:
            telemarketer_numbers.add(telephone_number)

    return telemarketer_numbers


def demo():
    telemarketer_numbers = sorted(get_telemarketer_numbers(calls, texts))
    print("These numbers could be telemarketers:")
    for telephone_number in telemarketer_numbers:
        print(telephone_number)


demo()

# Calculate Big O:
# call_numbers() => O(n)
# text_numbers() => O(n)
# for telephone_number in set_of_caller_numbers => O (n)
# check telephone_number is in telemarketer_numbers => O(n)
# add => O(1)
# sorted => O(n * log n)
# print => O(n)
# total: O(n * (n^2 + n * log n + 1))
