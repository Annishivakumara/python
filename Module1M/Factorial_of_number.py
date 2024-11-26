#QUESTION TITLE	Write a Python program to calculate the factorial of a given number using 
# a loop (without using any predefined functions). The program should prompt the user to input
#  a number and then compute its factorial
#PROBLEM STATEMENT	Factorial of number using loop
#CONSTRAINTS	Input Format:-
#The first line contains a single integer n (0 ≤ n ≤ 20), 
#which represents the number for which you need to 
#calculate the factorial.
#Output Format:-
 #A single integer representing the factorial of the input number n.
#PUBLIC TESTCASE	Input:-
#5
#Output:-
#120
number=int(input("Enter The Number: "))
fact=1
while number>0:
    fact=fact*number
    number-=1
print(fact)