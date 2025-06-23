"""How would you implement the Bubble Sort algorithm in Python
to sort a list of numbers in ascending order?
Give an example """

# Create a function that takes 2 parameters, one for the list to sort and
# the other a boolean to control sort direction
# if l_h=True(Ascending= Low to high), if l_h=False(Descending = high to low)

def bubble_sort(list1, l_h=True):
    n = len(list1)
    for i in range(n):
        for j in range(n-1):
            if l_h:
                # to sort in Ascending order
                result = list1[j] > list1[j+1]
            else:
                # to sort in Descending order
                result = list1[j] < list1[j+1]
            # check if result is True or False
            if result:
                list1[j], list1[j+1] = list1[j+1], list1[j]

sort = [2,5,1,5,4,34]
bubble_sort(sort)
print(f"Sorted Lower to Higher {sort}")
bubble_sort(sort, l_h=False)
print(f"Sorted Higher to Lower {sort}")


