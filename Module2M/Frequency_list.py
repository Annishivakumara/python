#QUESTION TITLE	Frequency of an item in the list
#PROBLEM STATEMENT	Given a list of integers, find all the elements that appear more than once.
#CONSTRAINTS	Input Format
#The first line contains an integer n, the number of elements in the list.
#The second line contains n space-separated integers.
#The list will contain at least one element.
#Number of Elements (n): 1 ≤ n ≤ 10^5 
#Values of Elements: -10^9 ≤ element ≤ 10^9
#Output Format:
#The program should output a list of integers that appear more than once in the input list. 
#The output list should not contain duplicates.
#PUBLIC TESTCASE	Sample Input
#6
#1 2 2 3 3 3
#Sample Output
#[2,3]
number=int(input("Enter The Input: "))
list1=list(map(int , input("Enter the List : ").split()))
repeated_element=[]
for i in list1:
   if i not in  repeated_element:
      for i in repeated_element:
          if i == repeated_element:
             repeated_element.append(list1[i])
print(repeated_element)
