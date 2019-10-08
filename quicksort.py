import math

def partition(list1, low, high):
    i = low - 1
    pivot = list1[high]
    for j in range(low, high):
        if list1[j] <= pivot:
            i += 1
            list1[i], list1[j] = list1[j], list1[i]
    list1[i+1], list1[high] = list1[high], list1[i+1]
    return i + 1

def quicksort(list1, low, high):
    if low < high:
        p = partition(list1, low, high)
        quicksort(list1, low, p - 1)
        quicksort(list1, p + 1, high)

l = [10, 7, 8, 9, 1, 5]
n = len(l)
quicksort(l, 0, n-1)
print(l)
