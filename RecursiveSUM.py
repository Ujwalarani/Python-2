"""Using recursion calculate sum of 1 to n numbers"""

def recur_sum(n):
    if n == 1:
        return 1

    return n + recur_sum(n-1)

num = int(input("Enter any positive number: "))

print(f"The sum of 1 to {num} numbers = {recur_sum(num)}")
