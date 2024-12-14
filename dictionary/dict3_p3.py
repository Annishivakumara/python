text=("Apple", "banana","apple","orange","banana", "apple")
#cleaned_stenatce=text.replace(",", " ").lower().split()
cleaned_sentence = text.replace(",", "").lower().split()  # Convert
res={}
for i in cleaned_sentence:
    key_=i
    value_=cleaned_sentence.count(i)
    res.update({key_: value_})
print(res)