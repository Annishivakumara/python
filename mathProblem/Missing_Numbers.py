#QUESTION TITLE	Find Missing Numbers
#PROBLEM STATEMENT	write a program to find and return all the missing numbers in sorted order.
#CONSTRAINTS	Input Format
#The first line contains an integer, n, which represents the maximum number in the full sequence (from1 to n).
#The second line contains space-separated integers, representing the list of numbers with some missing elements.

#1≤𝑛≤10^5
#≤n≤10^5
#Each integer in the list is unique and within the range from 1 to n.
#Output Format
#Print the missing numbers in ascending order, separated by spaces.
#If no numbers are missing, print No missing numbers.
#PUBLIC TESTCASE	Input:
#6
#1 2 4 6
#Output:
#3 5
number=int(input("ENter the number: "))
lis=list(map(int, input("Enter the elements: ").split()))
missing_num=[]
for i in range(1, number+1):
    if i not in lis:
        missing_num.append(i)
print(*(missing_num))