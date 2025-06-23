"""Implement a recursive function to calculate the factorial of a non-negative integer.
Instructions:
Write a recursive function factorial(n) that returns the factorial of the non-negative integer n.
The factorial of n (denoted as n!) is defined as:
n! = n * (n-1)! for n > 0
0! = 1
Write test cases to verify the function works correctly for different values of n."""

try:
# Create a function to handle factorials
    def factorial(number):

        #Create an if statement to handle if the num is less than or equal to or something else
        if number < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        elif number == 0:
            return 1
        else:
            return number * factorial(number - 1)

    num = int(input("Enter a number: "))

    print(factorial(0))
    print(factorial(1))
    print(factorial(5))
    print(factorial(num))
except ValueError as e:
    print(e)



