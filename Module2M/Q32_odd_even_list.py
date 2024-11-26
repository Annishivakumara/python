#UESTION TITLE	Separate list of numbers into odd and even list
#PROBLEM STATEMENT	Write a program that separates list of numbers into odd and even numbers and print separately
#CONSTRAINTS	Input Format
#prompt the user to input a numbersseparated by comma, which will then be converted into a list of integers
#Output Format:
#print two separate lists: one for the odd numbers and one for the even numbers.
#PUBLIC TESTCASE	Sample Input
#1,2,3,4,5,6
#Sample Output
#even :[2,4,6] 
#odd :[1,3,5]
lis=list(map(int, input("Enter the Input: ").split(',')))
even_list=[]
odd_list=[]
for i in lis:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)