number=int(input("Enter The Total Input: "))
for i in range(number):
    x,y,z=list(map(int,input("enter the input: ").split()))
    cat_a=abs(x-z)
    cat_b=abs(y-z)
    if cat_a<cat_b:
        print("A wins")
    elif cat_b<cat_a:
        print("B wins")
    else:
        print("Mouse wins")