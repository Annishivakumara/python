#QUESTION TITLE	Given a string, count how many vowels (a, e, i, o, u) it contains.
#PROBLEM STATEMENT
# Write a Python Program to Count how many Vowels is contains in a string.
#ONSTRAINTS	The string may contain any characters, including spaces, punctuation, or
#  other non-alphabet symbols. We only count vowels (a, e, i, o, u, A, E, I, O, U).
#PUBLIC TESTCASE	Input:
#"apple"
#Output:
#2
String = input("Enter the String: ").lower()
vowels='aeiou'
count=0
for i in String:
    if i in vowels:
        count+=1
print(count)