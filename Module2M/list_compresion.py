#Question 22
#QUESTION TITLE	List Comprehensions
#PROBLEM STATEMENT	Write a Python program that generates the list of squares using list comprehension.
#CONSTRAINTS	Input:
#A single integer N (1 ≤ N ≤ 1000)
#Output: 
#A list containing the squares of numbers from 1 to N, inclusive.
#PUBLIC TESTCASE	Input: 
#5 
#Output:
#[1, 4, 9, 16, 25]
number=int(input("Enter the Input: "))
square=[ i**2 for i in range(1,number+1) ]
print(square)