#QUESTION TITLE	Find Maximum Element in a List
#PROBLEM STATEMENT	Write a Python Program to find the maximum number in a list.
#CONSTRAINTS	Number of Elements (n): 1 ≤ n ≤ 10^5 
#Values of Elements: -10^9 ≤ element ≤ 10^9
#PUBLIC TESTCASE	Input:
#5
#1 2 3 4 5
#Output:
#5
n=int(input("Enter The Number: "))
list1=list(map(int, input("Enter The Input list: ").split()))
max_num=list1[0] # 1 2 3 4 5   
for i in  list1: # 1  # 2 
    if  i>max_num: #1 > 1  # 2>1   # 3>2
        max_num=list1[i] # 2==max
print(max_num)