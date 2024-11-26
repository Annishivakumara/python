#QUESTION TITLE	Find Common Elements Between Two Lists Without Duplicates
#PROBLEM STATEMENT	Given two lists of integers, write a Python program to find and display the
# common elements between them,
#Without  duplicates, in the order they appear in the first list.
#CONSTRAINTS	Input Lists:
#•	Both lists contain integers separated by spaces.
#•	Each integer in the lists is within the range -10^9 to 10^9 inclusive.
#•	The lengths of the lists, N (for list1) and M (for list2), are both between 1 and 100,000.
#Output:
#•	A list of common elements between the two input lists, without duplicates, displayed in the order
#they appear in the first list.
#PUBLIC TESTCASE	Input: 
#1 2 3 4 5
#4 5 6 7
#Output: 
#[4, 5]
list1=list(map(int, input("Enter The List1 Elements: ").split()))
list2=list(map(int, input("Enter The List2 Elements: ").split()))
common_elements=[]
for i in list1:
    for j in list2:
        if i==j and i not in  common_elements:
           # or  if i not in common_elements:
                common_elements.append(i)
print(common_elements)