# Designed to calculate averages using code from scratch
# Tries not to rely on built in and external libraries as much as possible
# https://github.com/chriskanedev/year-1-uni/

import operator  # Used in the mode() function


def median(x):
    listlen = len(x)  # Get the amount of values in the list

    # Check if listlen is even or odd
    if listlen % 2 == 0:  # Even
        return medianeven(x, listlen)
    else:  # Odd
        return medianodd(x, listlen)


def medianeven(x, listlen):
    x = sorted(x)  # Sort the list from lowest to highest value

    median_left = (listlen / 2) - 1  # Find the position in the list at the top of the lower half
    median_right = (listlen / 2)  # Find the position in the list at the bottom of the upper half

    median_left = x[
        int(median_left)]  # Use the position in the list to find the value at the top of the lower half of the list
    median_right = x[
        int(median_right)]  # Use the position in the list to find the value at the bottom of the upper half of the list

    # Add these two values together then, divide by 2 to find the middle value between the two
    median = (median_left + median_right) / 2
    return median


def medianodd(x, listlen):
    x = sorted(x)  # Sort the list from lowest to highest value
    median_position = (listlen // 2)  # Find the position where the median lies in the list
    median = x[median_position]  # Get that median value and store it in a variable so it can be returned
    return median


def mode(x):
    mode_tracker = {}  # Make a dict to keep track of how many times a value appears
    for value in x:  # Iterate over each value in the original list
        if value in mode_tracker:
            mode_tracker[value] += 1
        else:
            mode_tracker[value] = 1

    mode_tracker = dict(sorted(mode_tracker.items(), key=operator.itemgetter(1), reverse=True))  # Sort the tracker dict
    # in descending order so that the key that appears the most often is at the start
    mode = list(mode_tracker.keys())[0]  # Find the first key in the list (the mode)
    return mode


def mean(x):
    running_total: int = 0
    for value in x:
        running_total += value

    mean = running_total / len(x)
    return mean


def range(x):
    highest = find_highest(x)
    lowest = find_lowest(x, highest)
    range = highest - lowest
    return range


def find_highest(x):
    running_highest = x[0]
    for value in x:
        if value > running_highest:
            running_highest = value
    return running_highest


def find_lowest(x, highest):
    running_lowest = highest
    for value in x:
        if value < running_lowest:
            running_lowest = value
    return running_lowest


# Used for testing the functions
x = [60, 80, 80, 40, 60, -100, 60, 80, 40, 80, 80, 20]
print("\n", median(x))
print("\n", mode(x))
print("\n", mean(x))
print("\n", range(x))

