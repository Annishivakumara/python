#QUESTION TITLE	Count ofitems in a list
#PROBLEM STATEMENT	write a Python program that will count the number of items in the shopping cart list and display the result. 
#CONSTRAINTS	Input:
#Take a list of items separated by comma

#Output:
#The total number of items in a list.
#PUBLIC TESTCASE	Input: laptop,headphones,mouse,keyboard
#Output: 4
list1=list(input("Enter the list: ").split())
count=0
for i in list1:
    if i == ',':
        count+=1
        
print(count)