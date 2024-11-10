print("This is input and output  work \n ")

boss=input("Boss name: ")
boss_age=int(input("Boy Age: "))
miss=input("Miss Name: ")
miss_age=int(input("Miss Age: "))

print(boss)
print(miss)

# diffrence between boy age and girl age 
age_def=abs(boss_age-miss_age)
#abs will helps to convert to - to +

#cancatination 
# Adding both name  using  and not supported to to cancatinate with 
print(boss+ "Loves" +miss+" and age " + str(age_def))

# f- String formated String  using 


#Error because of in python All inputs are String so we need to convert to int
print(f"{boss}   + lovees + { miss}.and diffrence between agem {age_def} ")

#repeatation
repet="Warning"
print(repet*7)
#String Method
#String upper
print(repet.upper())
#String Lower
print(repet.lower())
#String strip
print(repet.strip())
#replacing the defined strin name 
print(repet.replace("Warning","Error"))

#finfing the length
print(len(repet))

#String Access
print(repet[5])
#Slicing 
print(repet[0:5])
#reverse slicing
print(repet[-2])
#step fuction
print(repet[::3])

#escape function
s="SHUVU"

print("Hello\tPython")