#Group Words by Their Length
text=input("Enter The Input: ").split()
length_group={}

for words in text:
    length=len(text)
    if length in length_group:
        length_group[length].append(words)
    else:
        length_group[length]=[words]

print("Words By their Length: ")
for length,group in length_group.items():
    print(f"{length},")