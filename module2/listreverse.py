#Problem Statement:
#Write a Python program that takes a sentence as input and extracts the first letter 
# of each word to create an abbreviation or acronym.

#Input Format Description:
#The first line contains a sentence, which may consist of multiple words.
#Example Input:
#Kalyani Govt. Eng. College
#Output Format Description:
#The output should be a string that contains the first letter of each word in the sentence.
#Example Output:
#KGEC

#Test Cases:
#Test Case 1:
#Input:
#Kalyani Govt. Eng. College
#Output: KGEC
#Explanation: The first letter of each word is """"K"""", """"G"""", """"E"""", and """"C"""".

senetance=input("Enter the String: ")
words=senetance.split()
appears=""
for i in words:
    appears+=i[0]
print(appears)