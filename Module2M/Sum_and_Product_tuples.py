#QUESTION TITLE	Calculate Sum and Product of Elements in a Tuple
#PROBLEM STATEMENT	Write a Python program to input a tuple of numbers and calculate both the sum 
#and the product of all elements.
#CONSTRAINTS	Input Tuple:
#•	The tuple contains integers separated by spaces.
#•	Each integer in the tuple is within the range -10^6 to 10^6 inclusive.
#•	The length of the tuple, denoted as N, is between 1 and 1000.
#Output:
#•	The sum of all elements in the tuple.
#•	The product of all elements in the tuple.
#PUBLIC TESTCASE	Sample Input:
#1 2 3 4
#Sample output :
#10, 24
tuple1=tuple(map(int , input("Enter The Input: ").split()))
N=len(tuple1)+1
sum=0
product=1
for i in tuple1:
        sum+=i
        product*=i
print("sum: ", sum)
print("pro: ",product)
       