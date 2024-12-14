import math
def  add_numbers(*num):
       print(type(num))
       return sum(num)
       for i in  range(2,num):
            print( math.sqrt(i))

print(add_numbers(5,2,3,4))