#Q 26	Count Vowels and Consonants
#PROBLEM STATEMENT	Write a program to count the number of vowels and consonants in a given string.
#CONSTRAINTS	1≤length of 𝑠≤10^5
#1≤length of s≤10^5
# The string s contains only lowercase letters (a-z).
#PUBLIC TESTCASE	Input:
#Hello
#Output:
#2 3
String=input("Enter The String: ").lower()
vowels='aeiou'
vowel_count=0
conso_count=0
for i in String:
    if i in vowels:
        vowel_count+=1
    else:
        conso_count+=1
print("Vowel Count: ",vowel_count)
print("Consonent Count: ", conso_count)