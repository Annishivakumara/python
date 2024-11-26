#QUESTION TITLE	print a list of student names in alphabetical order by removing the duplicates
#PROBLEM STATEMENT	Write a program to print a list of student names in alphabetical order by 
#removing the duplicates
#CONSTRAINTS	Input Format
#prompt the user to input a student names separated by comma, which will then be converted into a list.
#Output Format
#print a list of student names in alphabetical order by removing the duplicates
#PUBLIC TESTCASE	Sample Input
#Alice,Bob,Alice,Charlie,Bob,Alice
#Sample Output
#["Alice","Bob","Charlie"]
lis=list(input("Enter the List: ").split())
unique_list=[]
for i in lis:
    if i not in unique_list:
                 unique_list.append(i