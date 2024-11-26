#QUESTION TITLE	Sum of Even and Odd Elements
#PROBLEM STATEMENT	Write a program to calculate the sum of even numbers and the sum of odd numbers separately.
##CONSTRAINTS	Input :
#The first line contains an integer n, the number of elements in the list.
#The second line contains n space-separated integers. Output: 
#Print two space-separated integers: the sum of even numbers and the sum of odd numbers.
#PUBLIC TESTCASE	Input:
#5
#1 2 3 4 5
#Output:
#6 9
n= int(input("enter the  input: "))
numbers=list(map(int , input("ENter the list ").split()))
even_sum=0
odd_sum=0
for i in numbers:
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print(f"Even Number sum:{even_sum}")
print(f"Odd Number Sum: {odd_sum} ")