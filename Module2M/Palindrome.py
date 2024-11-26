#QUESTION TITLE	Check if a Sentence is a Palindrome (Ignoring Spaces and Punctuation)
#PROBLEM STATEMENT	A user is entering text and wants to know if the sentence is a palindrome, ignoring 
# spaces and punctuation.
#CONSTRAINTS	Input Sentence:
#•	The input string can include letters, numbers, spaces, and punctuation.
#•	The length of the string is between 1 and 1000 characters inclusive.
#•	Case is insensitive, and only alphanumeric characters are considered for palindrome checking.
#Output:
#•	Print "Palindrome" if the sentence is a palindrome.
#•	Print "Not a Palindrome" if the sentence is not a palindrome.
#PUBLIC TESTCASE	
# Sample Input
#"A man, a plan, a canal, Panama"
#Sample Output
#"Palindrome"
sentence = input("Enter Input: ")
filtered_sentence = ""
reversed_sentence = ""
for char in sentence:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
        if 'A' <= char <= 'Z':  
            filtered_sentence += chr(ord(char) + 32)
        else:
            filtered_sentence += char
for i in range(len(filtered_sentence) - 1, -1, -1):
    reversed_sentence += filtered_sentence[i]
if filtered_sentence == reversed_sentence:
    print("Palindrome")
else:
    print("Not a Palindrome")		
		
		
		
		
		
		
		
		
		
		
		
		