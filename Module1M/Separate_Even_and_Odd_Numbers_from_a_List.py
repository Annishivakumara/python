#QUESTION TITLE	Separate Even and Odd Numbers from a List
#PROBLEM STATEMENT	Given a list of integers, separate the even numbers and odd numbers into two separate lists.
#CONSTRAINTS	
# Input: A list of integers, for example: 1 2 3 4 5 6 7 8 9 10 
# Output: Two lists: one containing all the even numbers and one containing all 
# the odd numbers from the input list.
#PUBLIC TESTCASE	
#Input: 1 2 3 4 5 6 7 8 9 10
#Output:
#Even numbers: [2, 4, 6, 8, 10]
#Odd numbers: [1, 3, 5, 7, 9]
list1=list(map(int, input("Enter The Number: ").split()))
Even_number=[]
Odd_number=[]
for i in  list1:
    if i%2==0:
        Even_number.append(i)
    else:
        Odd_number.append(i)
print("Even Sum: ",Even_number)
print("Odd Sum: ",Odd_number)