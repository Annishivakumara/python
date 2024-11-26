#"Imagine you are managing the order of tasks on your daily to-do list. 
#You want to reverse the order of your tasks, such that the last task becomes the first 
#and the first task becomes the last. This helps you reprioritize tasks for the day, 
#especially when plans change.

#4.Problem:
#Write a program that takes a list of n integers (representing tasks or items) 
# and reverses the order of the list. The solution should not use any built-in functions such as reverse().

#Input Format:
#First Line: An integer n, representing the number of elements in the list.
#Second Line: A space-separated list of n integers, representing the tasks or values.

#Test Cases:
#Test Case 1:
#Input:
#5
#1 2 3 4 5
#Output:
#5 4 3 2 1
tasks=int(input("Enter the Number: "))
arr=list(map(int , input("Enter  the List  values: ").split()))
reversed =[]
for i in range(tasks-1,-1,-1):
    reversed.append(arr[i])
print("Reversed list: " ,*reversed)