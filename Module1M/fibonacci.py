#QUESTION TITLE	 Fibnocci Series of Number
#PROBLEM STATEMENT	Write a Python program to generate the Fibonacci series up to a 
#given number n using a loop. The program should prompt the user to input the value of n, and 
#then print the Fibonacci series up to that number.
#CONSTRAINTS
# Input:-
#A single integer n
#Output:-
#The output should be a single integer, representing the n-th term in the Fibonacci sequence..
#PUBLIC TESTCASE	Input: -
#3
#Output:- 
#011
number=int(input("Enter The Input: "))
a=0
b=1
print(a,b,end=' ')
for i in range(2,number):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
