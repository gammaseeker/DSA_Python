import math

def merge(list1, list2):
    result = []
    left = 0
    right = 0
    while left < len(list1) and right < len(list2):
        if list1[left] < list2[right]:
            result.append(list1[left])
            left += 1
        else:
            result.append(list2[right])
            right += 1
    return result + list1[left:] + list2[right:]

def merge_sort(list1):
    if len(list1) == 1:
        return list1
    middle = math.floor(len(list1)/2)
    left = list1[0:middle]
    right = list1[middle:]
    return merge(merge_sort(left), merge_sort(right))

list1 = [5, 3, 1, 12, 6, 7]
print(merge_sort(list1))
