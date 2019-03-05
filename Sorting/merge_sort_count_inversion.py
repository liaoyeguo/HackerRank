#!/bin/python


def countInversions(arr):
    if len(arr) <= 1:
        return 0
    left = arr[0:len(arr) // 2]
    right = arr[len(arr) // 2:]

    inversion_left = countInversions(left)
    inversion_right = countInversions(right)

    # merge
    i, j, k = 0, 0, 0
    counter = 0
    len_left, len_right = len(left), len(right)
    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            counter += 1
        k += 1
    while i < len_left:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len_right:
        arr[k] = right[j]
        j += 1
        k += 1

    return counter + inversion_left + inversion_right


print countInversions([2, 1])
