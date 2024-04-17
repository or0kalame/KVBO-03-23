from random import randint, shuffle, choice
from math import log2


def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def selection_sort(data):
    for i in range(len(data) - 1):
        index_smallest = i
        for j in range(i + 1, len(data)):
            if data[j] < data[index_smallest]:
                index_smallest = j
        data[i], data[index_smallest] = data[index_smallest], data[i]
    return data


def gnomes_sort(data):
    n = len(data)
    i = 0
    while i < n - 1:
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
            if i > 0:
                i -= 1
        else:
            i += 1
    return data


def insertion_sort(data):
    n = len(data)
    for i in range(1, n):
        temp = data[i]
        j = i - 1
        while j >= 0 and temp < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = temp
    return data


def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid::]
        merge_sort(left)
        merge_sort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
    return data


def count_sort(input_array):
    high = max(input_array)
    low = min(input_array)
    
    count_array = [0] * (high - low + 1)

    for num in input_array:
        count_array[num - low] += 1

    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    output_array = [0] * len(input_array)

    for i in reversed(input_array):
        output_array[count_array[i - low] - 1] = i
        count_array[i - low] -= 1

    return output_array


def shell_sort(data):
    n = len(data)
    k = n // 2
    while k > 0:
        for i in range(k, n):
            temp = data[i]
            j = i
            while j >= k and data[j - k] > temp:
                data[j] = data[j - k]
                j -= k
            data[j] = temp
        k //= 2
    return data


def quick_sort(quick_list):
    n = len(quick_list)
    if len(quick_list) <= 1:
        return quick_list

    pivot = quick_list[len(quick_list) // 2]

    left = [x for x in quick_list if x < pivot]
    middle = [x for x in quick_list if x == pivot]
    right = [x for x in quick_list if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)




array = [randint(1, 40) for _ in range(10)]
print(f"Start array (unsorted): {array}")
print(f"Bubble sort: {bubble_sort(array.copy())}")
print(f"Selection sort: {selection_sort(array.copy())}")
print(f"Shaker sort: {shaker_sort(array.copy())}")
print(f"Gnome's sort: {gnomes_sort(array.copy())}")
print(f"Insertion sort: {insertion_sort(array.copy())}")
print(f"Merge sort: {merge_sort(array.copy())}")
print(f"Counting sort: {counting_sort(array.copy(), max(array))}")
print(f"Shell sort: {shell_sort(array.copy())}")
print(f"Quick sort: {quick_sort(array.copy())}")
