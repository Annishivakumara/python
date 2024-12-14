input_set={'apple', 'banana', 'cherry'}
vowels={'a', 'e', 'i', 'o', 'u'}
count=0
for i in input_set:
    for vowel in vowels:
        if vowel in i:
           count+=1
print(count)
