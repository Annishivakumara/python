#QUESTION TITLE	Given a list, find the sum of all elements in the list.
#PROBLEM STATEMENT	Write  a Python Program to print the Sum of all elements in a list
#CONSTRAINTS	Number of Elements (n): 1 ≤ n ≤ 10^5 
#Values of Elements: -10^9 ≤ element ≤ 10^9
#PUBLIC TESTCASE	Input
#5
#1 2 3 4 5
#Output
#15
n=int(input("Emter the Number: "))
lis=list(map(int, input("Enter The List Elements: ").split()))
sum=0
for i in lis:
    sum+=i
print(sum)