#Question 27
##QUESTION TITLE	List Rotation
#PROBLEM STATEMENT	Rotate a list to the right by k steps.
#CONSTRAINTS	Input Format
#The first line contains an integer n, the number of elements in the list.
#The second line contains n space-separated integers.
#The third line contains an integer k, the number of steps to rotate.
#Output Format
#Print the rotated list as a space-separated string.
#0≤k≤n
#Input:
#5
#1 2 3 4 5
#2
#Output:
#4 5 1 2 3
n=int(input("Enter the Input: "))
numbers=list(map(int , input("Enter the List : ").split()))
k=int(input("Enter the Integer:"))
k = k % n
rotated_list = arr[-k:] + arr[:-k]
print(" ".join(map(str, rotated_list)))