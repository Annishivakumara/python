#QUESTION TITLE	List of integer that contain even numbers
#and not divisible by 5.
#PROBLEM STATEMENT	Write a Python program that takes an input string in the format  1 to n, where n
#  is an integer greater than 1. 
#The program should generate a list of all numbers from 1 to n (inclusive) that satisfy the following conditions: The number is even. The number is not divisible by 5.
#CONSTRAINTS	
#Input: A single integer
#Output: A list of integers from 1 to  n  that are even and not divisible by 5.
#PUBLIC TESTCASE	INPUT:-
#1 to 30
#OUTPUT:-
#[2, 4, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 30]
text=input("Enter The Text: ").split()
start=int(text[0])
end=int(text[2])
new_text=[]
for i in range(start,end-1):
    if i%2==0 :
        new_text.append(i)
print(new_text)