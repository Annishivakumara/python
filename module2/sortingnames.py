'''
"5.Problem Statement:
Write a Python program that takes multiple names as input and sorts them in dictionary 
(lexical) order. After sorting, the program should output the names in ascending order.

Input Format Description:
The first line contains the number of names to be entered.
The following lines contain the names, one per line.
Example Input:
3
Arijit
Minaz
Arnab
Output Format Description:
The output should display the names in dictionary (lexical) order, each name on a new line.
Example Output:
Arijit
Arnab
Minaz
'''
names=int(input("Entr the Names size: "))
names_store=[]
for  i in range(names):
     names_store.append(input("Enter the names: "))
names_store.sort()
for name in names_store:
     print(name)