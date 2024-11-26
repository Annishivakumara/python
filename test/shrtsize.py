#"Find the Maximum Price"
#"""Imagine you are a manager in a clothing store. The store sells three different types of shirts, and you need to decide which shirt is the most expensive. The prices of the shirts vary, and your task is to compare these prices and determine which shirt is the
# highest-priced so you can make decisions about sales or promotions.
# You have three prices, and the program will help you determine which one is the largest,
# indicating the most expensive shirt."""
#Problem:
#Write a program that takes three prices as input and
#prints the highest one, helping you identify the most expensive shirt in the store.

#Test Case 1:
#Scenario: The prices of three shirts are 4, 7, and 2 dollars. You need to identify the most expensive shirt.

#Input:
#4, 7, 2
#Output:
#7
shirt1=int(input("Enter the  Shirt 1 prize: "))
shirt2=int(input("Enter the shirt 2 prize: "))
shirt3=int(input("Enter the  Shirt 3 Prize: "))

if shirt1>=shirt2 & shirt1<=shirt3:
    print(f"Shirt 1 is Heighest prize:- {shirt1}")
elif shirt2>=shirt1 & shirt2>shirt3:
    print(f"Shirt 2 is Heighest prize:- {shirt2}")
else:
    print(f"Shirt 3 is Heighest prize:- {shirt3}")