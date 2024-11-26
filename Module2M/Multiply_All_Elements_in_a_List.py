#QUESTION TITLE	Multiply All Elements in a List
#PROBLEM STATEMENT	Write a  program is to calculate the product of all elements
#  in the list and print the result.
#CONSTRAINTS	
#1≤𝑛≤10^3
#−10^3≤element≤10^3
#PUBLIC TESTCASE	Input:
#4
#1 2 3 4
#Output:
#24
n=int(input("Enter the input: "))
list1=list(map(int, input("Enter The Input: ").split()))
product=1
for i in list1:
     product*=i
print("Multiplied Value: ",product)