#Count Unique Words in a List
text=list(input("Enter The List String ").split())
unique_word={}
for  word in text:
   # if unique_word[word]=unique_word[word].get(word,0)+1:
   if word.isalpha():
     if word in unique_word:
            unique_word[word]+=1
     else:
           unique_word=1
print("Unique Words")
for words,count in unique_word[word].items():
       print(f"{words} :{count}")
        