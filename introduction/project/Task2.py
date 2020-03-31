"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


# get total spend time for each telephone number and
# save it into a defaultdict with format: {key: telephone_number, value: total_time}
def get_total_time_on_each_telephone_number(call_list):
    total_time_on_each_telephone_number = defaultdict(int)
    for call in call_list:
        for i in range(2):
            total_time_on_each_telephone_number[call[i]] += int(call[3])
    return total_time_on_each_telephone_number


def telephone_number_with_longest_time(call_list):
    total_time_on_each_telephone_number = get_total_time_on_each_telephone_number(call_list)

    telephone_number, longest_time = max(total_time_on_each_telephone_number.items(), key=lambda x: x[1])
    return telephone_number, longest_time


def demo():
    telephone_number, longest_time = telephone_number_with_longest_time(calls)
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(telephone_number,
                                                                                              longest_time))


demo()

# Calculate Big O:
# get_total_time_on_each_telephone_number(call_list) => O(n * 2 + 1)
# max(): O(n)
# total: O(2 * n + n + 1)
# O(n)
