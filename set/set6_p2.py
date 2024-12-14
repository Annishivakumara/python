lis=["Apple","Banana", "Mango", 
    "Banana", "Mango", "Orange",
    "Apple", "Orange" , "Pappaya"]
all_words=set()
repeated_words=set()

for i in lis:
      word=set(i.split())
      new_repeated=(str(word) + str(all_words))
      all_words.update(word)  #Unique The Elements 
      repeated_words.update(new_repeated)
print(all_words-repeated_words)
