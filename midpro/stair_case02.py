row=int(input("Enter The Rows: "))
for i in range(1,row+1):
    spaces=" "*(row-1)
    hashtag="#"*(i)
    print(spaces+hashtag)