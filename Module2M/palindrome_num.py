#QUESTION TITLE	Palindrome
#PROBLEM STATEMENT	Given a list, check whether the given list of elements are palindrome or not. (Reading the elements from forward and backward direction) 
#CONSTRAINTS	Input Format
#The first line contains an integer n, the number of elements in the list.
#The second line contains n space-separated integers.
#The list will contain at least one element.
#Number of Elements (n): 1 ≤ n ≤ 10^5 
#Values of Elements: -10^9 ≤ element ≤ 10^9
#Output Format:
#Print True if list is palindrome otherwise False.
#PUBLIC TESTCASE	Sample Input
#5
#1 2 3 4 5
#sample Output
#False
#EXPLANATION:
#When you read elements in the list from forward and backward direction it is not same. So, the output is false.
list1=list(map(int , input("Enter The List values: ").split()))
if list1==list1[::-1]:
    print("palindrome ")
else:
    print("Not palindrome ")