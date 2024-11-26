#QUESTION TITLE	Count Occurrences of Each Element
#PROBLEM STATEMENT	count the occurrences of each element and display them.
#CONSTRAINTS	Input Format
#The first line contains an integer n, the number of elements in the list.
#The second line contains n space-separated integers.
#Output Format
#Print each unique element followed by its count, in the order of their first appearance.
#PUBLIC TESTCASE	Input:
#7
#1 2 2 3 3 3 4
#Output:
#1 1
#2 2
#3 3
#4 1
n=int(input("Enter the N:  "))
numbers=list(map(int, input("Enter The List Elements: ").split()))
unique_element=[]
count=[]
for i in  numbers:
     if  i in unique_element:
          index=unique_element.index(i)
          count[index]+=1
     else:
         unique_element.append(i)
         count.append(i)
for i in range(len(unique_element)):
     print(unique_element[i] , count[i])