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
    incoming_call_numbers = []
    receiving_call_numbers = []
    for call in call_list:
        if call[0] not in incoming_call_numbers:
            incoming_call_numbers.append(call[0])
        if call[1] not in receiving_call_numbers:
            receiving_call_numbers.append(call[1])
    return incoming_call_numbers, receiving_call_numbers


def text_numbers(text_list):
    sending_text_numbers = []
    receiving_text_numbers = []
    for text in text_list:
        if text[0] not in sending_text_numbers:
            sending_text_numbers.append(text[0])
        if text[1] not in receiving_text_numbers:
            receiving_text_numbers.append(text[1])
    return sending_text_numbers, receiving_text_numbers


def list_of_telemarketers_number(call_list, text_list):
    list_of_numbers = []

    incoming_call_numbers, receiving_call_numbers = call_numbers(call_list)
    sending_text_numbers, receiving_text_numbers = text_numbers(text_list)

    for telephone_number in incoming_call_numbers:
        if telephone_number not in receiving_call_numbers and telephone_number not in sending_text_numbers and telephone_number not in receiving_text_numbers and telephone_number not in list_of_numbers:
            list_of_numbers.append(telephone_number)

    return list_of_numbers


def demo():
    list_of_numbers = sorted(list_of_telemarketers_number(calls, texts))
    print("These numbers could be telemarketers:")
    for number in list_of_numbers:
        print(number)


demo()


# Calculate Big O:
# call_numbers() => O(n * (a + b) + 1)
# text_numbers() => O(n * (c + d) + 1)
# for telephone_number in incoming_call_numbers => O (a)
# check telephone_number => O(b + c + d + k)
# append => O(1)
# print => O (k)
# total: O(n * (a + b + c + d) + a * (b + c + d + k) + k + 1)
# O(n * m + q * p + k)

