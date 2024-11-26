#PROBLEM STATEMENT	Ask input from user .Find the uppercase letter inside string using predefined function.
#CONSTRAINTS	Input Format:-
#The first line contains a single string s, which may include both lowercase and uppercase alphabets. 
#The string will have a length between 1 and 100 characters.
#Output Format:-
#A list of uppercase letters found in the input string.
#PUBLIC TESTCASE	Input:-
#"PythonProgramming"
#Output:-
#['P', 'P']
String=input("Enter The Input: ")
new_String=[]
for i in String:
    if i==i.upper():
        new_String.append(i)
print(new_String)