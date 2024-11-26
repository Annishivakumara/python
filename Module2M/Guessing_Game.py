#QUESTION TITLE	Replace Vowels with Underscores for a Guessing Game
#PROBLEM STATEMENT	Create a program to replace vowels in a sentence with underscores to make a guessing game for children.
#CONSTRAINTS	Input Sentence:
#•	The input string may contain letters, spaces, numbers, and punctuation.
#•	The length of the string is between 1 and 1000 inclusive.
#•	Vowels are considered as a, e, i, o, u (case-insensitive).
#Output:
#•	A modified string where all vowels are replaced with underscores (_).
#	Non-vowel characters, including spaces and punctuation, remain unchanged.

#PUBLIC TESTCASE	Sample Input
#"Hello World"
#Sample Output
#"H_ll_ W_rld"
String=input("Enter The Input: ")
vowels='aeiouAEIOU'
new_string=' '
for i in String:
    if i in vowels:
        new_string+='_'
    else:
        new_string+=i
print(new_string)