#QUESTION TITLE	Sum of odd number
#PROBLEM STATEMENT	Write a Python program to calculate the sum of all odd numbers from 1 to a given number n using a for loop (without using any predefined functions). The program should prompt the user to input the value of n and then output the sum of all odd numbers from 1 to n
#CONSTRAINTS	•Input: A single integer  
#•Output: An integer representing the sum of all odd numbers from 1 up to n.
#PUBLIC TESTCASE
#INPUT:-
#1 to 10
#OUTPUT:-
#25
text=input("Enter The Number: ").split()
start=int(text[0])
end=int(text[2])
sum_=0
for i in range(start, end+1):
    if i%2==1:
        sum_+=i
print(sum_)