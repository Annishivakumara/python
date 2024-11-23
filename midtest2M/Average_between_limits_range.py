#QUESTION TITLE	Average between limits range.
#PROBLEM STATEMENT	Write a program that takes n numbers as input (representing student quiz scores), along with two limit numbers, and calculates the average of the scores that fall between the two limits, excluding the limits themselves. The limits are always limit1 and limit2, where limit1 is the lower bound and limit2 is the upper bound.
##CONSTRAINTS	Input Format: 
#First Line: An integer n, representing the number of elements in the list. 
#Second Line: A space-separated list of n integers, representing the numbers (e.g., student scores or values). 
#Third Line: An integer limit1, representing the lower limit (this number and numbers below it are excluded). 
#Fourth Line: An integer limit2, representing the upper limit (this number and numbers above it are excluded).
#Output Format:
#Print the average which is single integer.
#PUBLIC TESTCASE	Input: 
#5 
#1 2 3 4 5 
#2
#4 
#Output:3 
#Explanation: The numbers between limit1 = 2 and 
#limit2 = 4 are 3, so the average is 3.
n=int(input('Enter the List Elemenest: '))
scores=list(map(int,input("Enter the Scores: ").split()))
limit1=int(input("Enter the Lower Limit 1 : "))
limit2=int(input("Enter the Upper Limit 2 :"))
total=0
count=0
for score in scores:
    total+=score
    count+=1
if count>0:
    average=total//count
    print(average)
else:
    print(0)