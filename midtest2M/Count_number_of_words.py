#QUESTION TITLE	Count number of words
#PROBLEM STATEMENT	Write a Python program to count the number of words in a string while ignoring any extra 
# spaces between words. The program should consider the words separated by space.
#CONSTRAINTS	
#Input Format Description: 
#The first line contains a string, which may contain words. 
#Output Format Description: 
#The output should be the total number of words in the string.
#PUBLIC TESTCASE	Input: 
#Kalyani Goverment Engineering College 
#Output: 4
#Explanation: The string contains 4 words: "Kalyani", "Goverment", "Engineering", and "College".
words=input("Enter the Input String: ")
count=0
spaces=" "
for i in words:
    if  i ==" ":  # i in spaces : 
        count+=1
print(f"Number of Words In The Sentacnce: {count} ")