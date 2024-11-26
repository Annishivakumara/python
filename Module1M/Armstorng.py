#QUESTION TITLE	
#PROBLEM STATEMENT	Write a Python program to check whether a given number is an 
# Armstrong number or not. The program should prompt the user to input a number and
#  then output whether the number is an Armstrong number.
#CONSTRAINTS	Input Format:-
#The first line contains a single integer n (1 ≤ n ≤ 10000), which is the number to
#  check if it is an Armstrong number
#Output Format:-
#A string that either states "Armstrong Number" if the number is an Armstrong number or
#  "Not Armstrong Number" if it is not.
#PUBLIC TESTCASE	Input:-
#153
#Output:-
#Armstrong
number=int(input("Enter the Number: "))
original=number
result=0
length=len(str(number))
while number>0:
    digit=number%10
    pow_num=digit**length
    result=result+pow_num
    number//=10
if result==original:
    print("Armstrong Number: ")
else:
    print("Not Armstrong: ")