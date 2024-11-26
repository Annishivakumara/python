#QUESTION TITLE	First letter of each word
#PROBLEM STATEMENT	Write a Python program that takes a sentence as input and extracts the first letter of each word to create an abbreviation or acronym.
#CONSTRAINTS	Input Format Description: 
#The first line contains a sentence, which may consist of multiple words. 

#Output Format Description: 
#The output should be a string that contains the first letter of each word in the sentence
#PUBLIC TESTCASE	
# Input: 
#Kalyani Govt. Eng. College
#Output: 
# KGEC
#Explanation: The first letter of each word is ""K"", ""G"", ""E"", and ""C"".

String =input("Enter The Input Senteances: ")
acronym=""
new_word=True
for i in String:
    if i==" ":
       new_word=True
    elif  new_word:
          acronym+=i
          new_word=False
print(f"New Starting Word: {acronym}..")