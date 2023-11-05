#!/usr/bin/python3
"""
Finds peak in list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num greater than both left and right
    """
    if not list_of_integers:
        return None

    start = 0
    end = len(list_of_integers)-1

    if list_of_integers[start] > list_of_integers[start+1]:
        return list_of_integers[start]
    if list_of_integers[end] > list_of_integers[end-1]:
        return list_of_integers[end]

    mid = len(list_of_integers) // 2
    mid_val = list_of_integers[mid]

    if list_of_integers[mid - 1] < mid_val \
            and list_of_integers[mid + 1] < mid_val:
        return mid_val
    if mid_val < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[start:mid + 1])
    elif mid_val < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:end + 1])
    else:
        return list_of_integers[start]
