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
def lis_of_codes_from_bangalore(call_list):
    list_of_codes = []
    for call in call_list:
        for i in range(2):
            if call[0].startswith("(080)"):
                if call[1].startswith("(") and call[1].split("(")[1].split(")")[0] not in list_of_codes:
                    area_codes = call[1].split("(")[1].split(")")[0]
                    list_of_codes.append(area_codes)
                elif len(call[1].split(" ")) == 2 and call[1][0] in ["7", "8", "9"] and call[1].split(" ")[0] not in list_of_codes:
                    mobile_prefix = call[1].split(" ")[0]
                    list_of_codes.append(mobile_prefix)
                else:
                    continue
    return list_of_codes


def demo_part_a():
    list_of_codes = sorted(lis_of_codes_from_bangalore(calls))
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
        for i in range(2):
            if call[0].startswith("(080)"):
                calls_from_fixed_lines_in_bangalore.append(call[0])
                if call[1].startswith("(080)"):
                    calls_from_fixed_lines_in_bangalore_to_fixed_line_in_bangalore.append(call[1])

    return calls_from_fixed_lines_in_bangalore, calls_from_fixed_lines_in_bangalore_to_fixed_line_in_bangalore


def demo_part_b():
    a, b = percentage_of_calls_from_fixed_lines_in_bangalore(calls)
    if len(a) == 0 or len(b) == 0:
        percentage = 0
    else:
        percentage = round(len(b) / len(a) * 100, 2)
    print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
        percentage))


print(" --- Part B ---")
demo_part_b()

# Calculate Big O:
# part A:
# lis_of_codes_from_bangalore() => O(n * 2 * m + 1)
# print list_of_codes => O(m)
# total: O(2 * n * m + m + 1)
# O(k * n^2)

# part B:
# percentage_of_calls_from_fixed_lines_in_bangalore() => O(2 * n + 1)
# calculate percentage: O(1)
# total: O(2 * n + 2)
# O(k * n)
