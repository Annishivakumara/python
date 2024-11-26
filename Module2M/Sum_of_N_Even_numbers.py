#QUESTION TITLE	 Sum of N Even numbers
#PROBLEM STATEMENT	Write a program to calculate the sum of all even numbers up to a given number n.
#CONSTRAINTS	Input Format:
#•	Integer N
#•	N(0 ≤ N ≤ 1000)
#Output:
#•	The sum of all even numbers up to N.
#PUBLIC TESTCASE	Input:
#10
#Output:
#30
#EXPLANATION:
#2 + 4 + 6 + 8 + 10 = 30
numbers=int(input("Enter The Input: "))
even_sum=0
for i in range(0,numbers+1):
    if i%2==0:
        even_sum+=i
print(even_sum)