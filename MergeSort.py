"""Explain the Merge Sort algorithm and demonstrate its implementation in Python
to sort a list of strings in alphabetical order.
Give an example"""

def merge_sort(list1):
    # if the list have 1 or no elements that means its sorted
    if len(list1) <= 1:
        return list1

    # split the list into 2
    mid = len(list1) // 2

    # split and recursively sort both halves
    left_half = merge_sort(list1[:mid])
    right_half = merge_sort(list1[mid:])

    # merge the list back together
    return merge(left_half, right_half)

def merge(left, right):
    # merge both lists together into one
    result = []
    i = j = 0

    # comparing the elements from both the list and add the smaller one to result
    while i < len(left) and j < len(right):
        if left[i].lower() <= right[j].lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # this will add the remaining elements to the left of the list
    while i < len(left):
        result.append(left[i])
        i += 1

    # this will add the remaining elements to the right on the list
    while j < len(right):
        result.append(right[j])
        j += 1

    # this will return your merged list
    return result


words = ["Banana", "Apple", "Grapes", "Orange", "Cherry"]
sorted_list = merge_sort(words)
print()
print(sorted_list)