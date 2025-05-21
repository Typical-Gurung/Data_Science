def factorial_for_loop(n):
    result=1
    for i in range(2,n+1):
        result *=i
    return result
number=int(input('Enter the number'))
print(f'factorial of a number {number} using for loop: {factorial_for_loop(number)}')