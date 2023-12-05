'''Write a program that does the following

Declare an integer variable 
�
�
�
num and initialise it to a user defined input
Output to the console the factorial of 
�
�
�
num
Remember to use 'loops' for this problem
Factorial of a number n is the product of all the numbers from 1 to n
Factorial of a number(n) = 
�
×
(
�
−
1
)
×
.
.
.
2
×
1
n×(n−1)×...2×1'''
n = int(input())

i = 1
factorial = 1

while i <= n:
    factorial = i * factorial
    i = i + 1
    
print("The factorial of the given number is:", factorial)
