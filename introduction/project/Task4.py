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
    caller_numbers = set()
    receiver_numbers = set()
    for call in call_list:
        caller_numbers.add(call[0])
        receiver_numbers.add(call[1])
    return caller_numbers, receiver_numbers


def text_numbers(text_list):
    sender_text_numbers = set()
    receiver_text_numbers = set()
    for text in text_list:
        sender_text_numbers.add(text[0])
        receiver_text_numbers.add(text[1])
    return sender_text_numbers, receiver_text_numbers


def get_telemarketer_numbers(call_list, text_list):
    telemarketer_numbers = set()

    caller_numbers, receiver_numbers = call_numbers(call_list)
    sender_text_numbers, receiver_text_numbers = text_numbers(text_list)

    for telephone_number in caller_numbers:
        if telephone_number not in receiver_numbers \
           and telephone_number not in sender_text_numbers \
           and telephone_number not in receiver_text_numbers:
            telemarketer_numbers.add(telephone_number)

    return telemarketer_numbers


def demo():
    telemarketer_numbers = sorted(get_telemarketer_numbers(calls, texts))
    print("These numbers could be telemarketers:")
    for telephone_number in telemarketer_numbers:
        print(telephone_number)
    print(len(telemarketer_numbers))


demo()

# Calculate Big O:
# call_numbers() => O(n)
# text_numbers() => O(n)
# for telephone_number in set_of_caller_numbers => O (n)
# check telephone_number is in telemarketer_numbers => O(1)
# add => O(1)
# sorted => O(n * log(n))
# print => O(n)
# total: O(n + n + n * 1 + 1 + n * log(n) + n)
# O(n * log(n))
