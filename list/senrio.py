 # Initialize an empty list to store results
number=[]
for num in range(1,21): # Iterate over the range 
    number.append(
        "FIZZ BUZZ " if num%3==0 and num%5==0
        else "FIZZ" if num%3==0
        else "BUZZ" if num%5==0
        else num
    )
print(number , end='-')  # Print the final FizzBuzz list