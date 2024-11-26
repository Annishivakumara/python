#QUESTION TITLE	Basic Arithmetic Operations
#PROBLEM STATEMENT	Write a C program to perform a basic arithmetic operation on two integers based on 
# a given operator (+, -, *, /).
#CONSTRAINTS	The first line contains two integers a and b (1 ≤ a, b ≤ 100). The second line contains
#  a character op representing the operation (+, -, *, /).
##Print the result of the operation.
#PUBLIC TESTCASE	Input :10 5  +
#Output :15
num1=int(input("Enter the Number: "))
num2=int(input("Enter the Number: "))
op=input("Enter the Opearation +-/%: ")
if op=='+':
    print(num1+num2)
if op=='-':
    print(num1-num2)
if op=='*':
    print(num1*num2)
if op=='/':
    print(num1/num2)
