#"Program to Check if a Number is a Perfect Number
#Problem: A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding the number itself.
#  Given an integer n, check if it is a perfect number.
#Input: An integer n. 
#Output: Print ""Perfect Number"" if n is a perfect number; otherwise, print ""Not a Perfect Number"".
n = int(input("Enter an integer: "))
sum_of_divisors = 0
for i in range(1, n):
    if n % i == 0:
        sum_of_divisors += i

if sum_of_divisors == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")