#QUESTION TITLE	Remove Duplicates and Retain Original Order
#PROBLEM STATEMENT	Given a list of numbers with potential duplicates, 
#write a Python program to remove all duplicates and display the unique elements in the original order.
#CONSTRAINTS	Input:
#•	A list of integers separated by spaces.
#•	Each integer in the list is between -10^9 and 10^9 inclusive.
#•	The length of the list, denoted as 𝑁, is between 1 and 100,000.
#Output:
#•	A list containing only the unique integers from the input, displayed in their original order.

#PUBLIC TESTCASE	Input:
#5 8 5 3 9 3 8 2 1 7 9
#Output:
#[5, 8, 3, 9, 2, 1, 7]
list1_num=list(map(int , input("Enter the Numbers: ").split()))
unique_list=[]
for i in list1_num:
    if i not in unique_list:
         unique_list.append(i)  # in list append function is used to  add the element
print(unique_list)