#QUESTION TITLE	Given a list, reverse the order of its elements
#PROBLEM STATEMENT	Write a program that takes a list of integers and outputs the list in reverse order.
#CONSTRAINTS	Number of Elements (n): 1 ≤ n ≤ 10^5 
#Values of Elements: -10^9 ≤ element ≤ 10^9
#PUBLIC TESTCASE	
#Input
#5
#1 2 3 4 5
#Output
#5 4 3 2 1
n= int(input("Enter The in Number: "))
list1=list(map(int , input("Enter the list: ").split()))
start_index=len(list1)-1
end_index=0
new_list=[]
while start_index>=0:
      new_list.append(list1[start_index])
      start_index-=1
print(*(new_list))
