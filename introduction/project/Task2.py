"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

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
# save it into a dict with format: {key: telephone_number, value: total_time}
def total_time_on_each_telephone_number(call_list):
    total_time_dict = {}
    for call in call_list:
        for i in range(2):
            if call[i] not in total_time_dict:
                total_time_dict[call[i]] = int(call[3])
            else:
                total_time_dict[call[i]] += int(call[3])

    return total_time_dict


def telephone_number_with_longest_time(call_list):
    longest_time = 0
    telephone_number = None
    total_time_list = total_time_on_each_telephone_number(call_list)
    for key in total_time_list:
        if total_time_list[key] > longest_time:
            longest_time = total_time_list[key]
            telephone_number = key
    return longest_time, telephone_number


def demo():
    total_longest_time, telephone_number = telephone_number_with_longest_time(calls)
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(telephone_number,
                                                                                              total_longest_time))


demo()


# Calculate Big O:
# total_time_on_each_telephone_number(call_list) => O(n * 2 * m + 1)
# for key in total_time_list => O(m)
# compare and assign: O(1)
# total: O(2 * n * m + m + 1)
# O(k * n^2)
