lis=list(map(int, input('ENTER THE INPUT: ').split()))  # 1 2 3 
left_sum=0 # 0  
total_sum=0 # 0
for num in lis: # 1 
    total_sum+=num # 6
for num in lis:  # 1 
    current_digit=num # 1  2  3 
    right_sum=total_sum-left_sum-current_digit  # 6 - 0 - 1 = 5 6-1-2 =3 6-2-3 =1 
    if left_sum==right_sum:  #0==5  = no  1  == 3 3 ==1 no
          print("Yes It Is Equal: ")
          break
left_sum+=current_digit # 0+ 1 =1  1 + 2 =3  3 +1 =4
print(left_sum)  #  
print(total_sum) # 6