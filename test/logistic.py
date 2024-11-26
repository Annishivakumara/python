#"Imagine you're working in a logistics company that tracks the number of deliveries made by each truck. 
# Management wants to know which trucks have made an even number of deliveries so they can schedule those 
# trucks for maintenance or other tasks. You need to write a Python program that takes the number of trucks 
# and the corresponding deliveries made by each truck, and prints only the trucks that made an even number 
# of deliveries.

#Problem Statement:
#Write a Python program that takes two lines of input:

#The first line contains the number of trucks (N) – though this number is just to indicate how many numbers
# will follow and is not directly used.
#The second line contains N integers, representing the number of deliveries made by each truck.
#The program should print all even numbers from the list of deliveries.

#Input Format Description:
#The first line contains a single integer N (the number of trucks).
# second line contains N space-separated integers, where each integer represents the number of deliveries made by a truck.
#Example Input:
#5
##1 2 3 4 5 
#Output Format Description:
#The output will consist of space-separated even numbers from the list, printed in the order they appear.
#If no even numbers are found, no output is produced.
#Example Output:
#2 
trucks=int(input("Enter the Number of  Truck : "))
deliveries=list(map(int, input("Enter the Number of deliveries: ").split()))
even_number_trucks=[]
for i in deliveries:
    if i%2==0:
        even_number_trucks.append(i)
for i in even_number_trucks:
    print(i, end=',')