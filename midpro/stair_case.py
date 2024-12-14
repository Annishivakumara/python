rows=int(input("Enter The Number Of Rows: "))
for i in range(1, rows+1):
    spaces=" "*(rows-i)
    hashtag="#"*(i)
    print(spaces+hashtag)