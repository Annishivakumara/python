# Counting Occurrences 
text = "apple banana apple orange banana apple grape" 
words=text.split(); # Split the text into words \

# Initialize an empty dictionary for countin
word_count={}

# Count occurrences of each word 
for word in text:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
# Display the word count 
print("word Frequence")
for words,count in word_count.items():
    
    print(f"{words}: {count}",end=',') 

