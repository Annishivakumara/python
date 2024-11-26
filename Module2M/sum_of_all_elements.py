#QUESTION TITLE	Given a list find the sum of all elements in the list
#PROBLEM STATEMENT	Write a program to find the  sum of all elements  in the list
#CONSTRAINTS	Input:
#The first line contains an integer n, the number of elements in the list.
#The second line contains n space-separated integers.
#The list will contain at least one element.
#Number of Elements (n): 1 ≤ n ≤ 10^5 
#alues of Elements: -10^9 ≤ element ≤ 10^9
#Output:
#Print the sum of the elements in the list.
#PUBLIC TESTCASE	Input: 
#5
#1 2 3 4 5
#Output: 
#15
#EXPLANATION:
#The sum of items 1+2+3+4+5 is 15.
list1=list(map(int, input("Enter The List Elements: ").split()))
sum=0
for i in list1:
    sum+=i
print(sum)
