#QUESTION TITLE	Identify Trucks with Even Delivery Counts
##PROBLEM STATEMENT	Write a Python program that takes the number of trucks and their corresponding
# delivery counts, and prints the trucks that made an even number of deliveries.
#CONSTRAINTS	
# Input Format:
#•	The first line contains an integer N (number of trucks).
#•	The second line contains N space-separated integers representing the number of deliveries.
#Output Format:
#•	Print all even numbers (space-separated) from the list of deliveries in the order they appear.
#PUBLIC TESTCASE	Input: 
#5 
#1 2 3 4 5 
#Output: 
#2 4 
#Explanation: The even numbers are 2 and 4.
truks=int(input('Enter the Number: '))
delivery_counts=list(map(int, input("Enter the input List values: ").split()))
for i in delivery_counts:
    if i%2==0:
        print(f"Even  Numbers Saparated By Spaces: {i}")
