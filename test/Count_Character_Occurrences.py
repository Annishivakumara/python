#"Imagine you're working in a text analysis company that processes user reviews for a product.
#  Your task is to determine how many times a specific character appears in a given review text.
#  This information is useful for sentiment analysis, to understand the frequency of certain 
#  or emotional indicators. For example, if the character ""!"" appears frequently in a review, 
# it might indicate excitement. You need to create a program that takes a review (string) and a character 
# as input and returns how many times that character appears in the review.

#Problem Statement:
#Write a Python program that takes a
#  string and a character as input and outputs the number
#  of times the character appears in the string.

#Input Format Description:
#The first line contains a string, which is the review or the text.
#The second line contains a character, which you need to count in the string.
#Example Input:
#Priyankaa
#Output Format Description:
#The output will be an integer representing the number of times the given character appears in the string.
#Example Output:
#2
str1=input("Enter the String : ").lower()
char=input("Enter the Charcter: ")
count=0
for i in  str1:
    if i==char:
        count+=1
print(count)