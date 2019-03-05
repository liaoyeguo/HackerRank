#!/bin/python
from bisect import insort, bisect_right


def maximumSum(a, m):
    # calculate prefix
    prefix = []
    cur = 0
    for val in a:
        cur = (cur + val % m) % m
        prefix.append(cur)

    # find cheapest prefix[j] > prefix[i]
    result = max(prefix)
    ordered = [prefix[0]]
    for i in range(1, len(prefix)):
        index = bisect_right(ordered, prefix[i])
        if index != len(ordered):
            result = max(result, (prefix[i] - ordered[index] + m) % m)
        insort(ordered, prefix[i])
    return result


print maximumSum([3, 3, 9, 9, 5], 7)
