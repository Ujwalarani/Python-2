"""Implement a recursive function to compute the nth Fibonacci number.
Instructions:
Write a recursive function fibonacci(n) that returns the nth Fibonacci number.
The Fibonacci sequence is defined as:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1
Write test cases to verify the function works correctly for different values of n."""


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def fibonacci_num(n):
    result = []
    for i in range (n):
        result.append(fib(i))
    return result

if __name__ == "__main__":
    #number = 5
    # Ask user to enter a number
    number = int(input("Enter a number: "))
    final_result = fibonacci_num(number)
    for feb_seq in final_result:
        print(feb_seq, end=' ' )





