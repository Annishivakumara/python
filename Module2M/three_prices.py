#QUESTION TITLE	Highest of the three prices
#PROBLEM STATEMENT	Write a program that takes three prices as input and prints the highest one,
#  helping you identify the most expensive shirt in the store.
#CONSTRAINTS	Input Format:
#•	Three numbers representing the prices of the shirts.
#Output Format:
#•	A single number representing the most expensive shirt price.
#PUBLIC TESTCASE	Input: 4, 7, 2 
#Output: 7
#Explanation: The largest value among 4, 7, and 2 is 7.
price1,price2,price3=map(int,input("Enter The Input: ").split())
if price1>=price2 and price1>=price3:
    heighest=price1
elif price2>=price1 and price2>=price2:
    heighest=price2
else:
    heighest=price3
print("Heighest Price: ",heighest)