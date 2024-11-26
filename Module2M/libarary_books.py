#QUESTION TITLE	Find Available Books in a Library
#PROBLEM STATEMENT	A library stores information about available and checked-out books. 
#Given two lists, one with all books and one with checked-out books, write a Python program to find and display the books currently available.
#CONSTRAINTS	Input Lists:
#•	The first input is a space-separated string of all books, all_books.
#•	The second input is a space-separated string of checked_out_books.
#•	Both lists may contain between 1 and 1000 books.
#Output:
#•	A list of books currently available in the library.
#PUBLIC TESTCASE	Sample Input
#Book1 Book2 Book3 Book4
#Book2 Book4
#Sample Output
#['Book1', 'Book3']
all_books=list(input("Enter the String: " ).split())
checked_books=list(input("Enter the Sting Books: ").split())
available_books=[]
for i in all_books:
    if i not in checked_books:
         available_books.append(i)
print(available_books)
