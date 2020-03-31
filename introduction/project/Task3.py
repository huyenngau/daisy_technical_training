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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


# part A
def get_area_codes(number):
    if number.startswith("("):
        return number.split("(")[1].split(")")[0]
    elif len(number.split(" ")) == 2 and number[0] in ["7", "8", "9"]:
        return number.split(" ")[0]
    else:
        return "140"


def get_receiver_area_codes_from_bangalore(call_list):
    receiver_area_codes_from_bangalore = set()
    for call in call_list:
        caller_number = get_area_codes(call[0])
        if caller_number == "080":
            receiver_number = get_area_codes(call[1])
            if receiver_number != "140":
                receiver_area_codes_from_bangalore.add(receiver_number)

    return receiver_area_codes_from_bangalore


def demo_part_a():
    list_of_codes = sorted(get_receiver_area_codes_from_bangalore(calls))
    print("The numbers called by people in Bangalore have codes:")
    for code in list_of_codes:
        print(code)


print(" --- Part A ---")
demo_part_a()


# part B
def percentage_of_calls_from_fixed_lines_in_bangalore(call_list):
    calls_from_fixed_lines_in_bangalore = []
    calls_from_fixed_lines_in_bangalore_to_fixed_line_in_bangalore = []
    for call in call_list:
        caller_number = get_area_codes(call[0])
        if caller_number == "080":
            calls_from_fixed_lines_in_bangalore.append(caller_number)
            receiver_number = get_area_codes(call[1])
            if receiver_number == "080":
                calls_from_fixed_lines_in_bangalore_to_fixed_line_in_bangalore.append(call[1])

    a = len(calls_from_fixed_lines_in_bangalore)
    b = len(calls_from_fixed_lines_in_bangalore_to_fixed_line_in_bangalore)
    if a == 0 or b == 0:
        percentage = 0
    else:
        percentage = round(b / a * 100, 2)
    return percentage


def demo_part_b():
    percentage = percentage_of_calls_from_fixed_lines_in_bangalore(calls)
    print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
        percentage))


print(" --- Part B ---")
demo_part_b()

# Calculate Big O:
# part A:
# get_receiver_area_codes_from_bangalore() has 1 loop => O(n)
# sorted: O(n * log(n))
# loop to print code: O(n)
# total: O(n + n * log (n) + n)
# O(n * log (n))

# part B:
# percentage_of_calls_from_fixed_lines_in_bangalore() has 1 loop => O(n)
# calculate percentage: O(1)
# total: O(n + 1)
# O(n)
