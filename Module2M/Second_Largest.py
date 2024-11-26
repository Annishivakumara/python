#QUESTION TITLE	Second Largest element in the list
#PROBLEM STATEMENT	Write a program to find the second largest element in the list.
#CONSTRAINTS	Input Format:
#The first line contains an integer n, the number of elements in the list.
#The second line contains n space-separated integers.
#The list will contain at least 2 elements.
#Number of Elements (n): 1 ≤ n ≤ 10^5 
#Values of Elements: -10^9 ≤ element ≤ 10^9
#Output Format:
#Print the second largest element in the list.
#PUBLIC TESTCASE	Sample Input:
#5
#1 2 3 4 5
#Sample output:
#4
#EXPLANATION:
#The sorted list of items will be 5 4 3 2 1 in the descending order and 4 becomes the second largest element in the list.
n=int(input("Enter the List element: "))
list1=list(map(int , input("Enter The Element: ").split())) # 1 2 3 4 5
list1.sort(reverse=True) # 5 4 3 2 1
for i in range(1,len(list1)):  # 5 4 3 2 1
    if list1[i]!=list1[0]:  # 4 not equal to 5
        print(list1[i]) 
        break