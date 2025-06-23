"""What is the time complexity of the Quick Sort algorithm,
and how would you implement it in Python?
Give an example"""

#import random module so the pivot can be selected randomly
import random

def quick_sort(list1, pivot_log=None):
    if pivot_log is None:
        pivot_log = []
    if len(list1) <= 1:
       return list1

    # choose random pivot
    pivot_index = random.randint(0, len(list1) - 1)
    pivot = list1[pivot_index]
    pivot_log.append(pivot)  # save the pivot value

    # Exclude the pivot from sublists using slicing + filtering
    # Elements left = All elements before the pivot + All elements after the pivot
    elements_remaining = list1[:pivot_index] + list1[pivot_index + 1:]

    left = [x for x in elements_remaining if x <= pivot]
    right = [x for x in elements_remaining if x > pivot]
    return quick_sort(left, pivot_log) + [pivot] + quick_sort(right, pivot_log)

data = [10,5,0,6,2,25,3]
pivot_values = []
result = quick_sort(data, pivot_values)
print(f"\nSorted list: {result}")
print("\nFor every recursion the random pivot value selected is: ")
for p in pivot_values:
    print(p)
