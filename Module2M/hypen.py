#Question 20
#QUESTION TITLE	Replace space with hyphen(-)
#PROBLEM STATEMENT	Write a program which replaces all spaces in the string s with hyphen.
#CONSTRAINTS	Input Format
#The first line contains a string s.
#The input may contain spaces.
#The string may contain any characters, including spaces, punctuation, or other non-alphabet symbols.
#Output Format:
#The program should output a string where all spaces are replaced by hyphens (-).
#PUBLIC TESTCASE	Sample Input
#“hello world”
#Sample Output
#“hello-world”
#EXPLANATION:
#The space between two words is replaced by hyphen.
String=input("Enter The String: ")
new_string=''
for i in String:
    if i==' ':
       new_string+='-'
    else:
        new_string+=i
print(new_string)