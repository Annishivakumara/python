'''#"You are developing a text analysis tool for an educational application that helps students 
improve their reading and writing skills. One of the features is to provide feedback on the vowel
usage in their written assignments.Given a student’s written paragraph, such as ""The quick brown fox 
jumps over the lazy dog."", how would you provide the program to count the number of vowels in the paragraph?

Input Format:
The program will prompt the user to input a sentence or paragraph.
The input can contain any combination of characters, including spaces and punctuation.
sample input: the cute picture

Output Format:
The program should count and print the total number of vowels (a, e, i, o, u)in the given sentence or paragraph.
sample output: 6
'''
sentance=input("Enter the sentance input:- ")
vowels="aeiou"
count=0
for i in sentance:
    if i in vowels:
       count+=1
print("Toatl Number of Vowels: ", count)