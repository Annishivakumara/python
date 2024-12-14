scores=(
    (85,90,88),
    (78,81,85),
    (92,88,91)
)
res=[]
for i in scores:
    sum_=sum(i)  # sum=sum+i
    num_items=len(i) #num_items+=1
    avg=sum_/num_items  
    res.append(avg)
formated=tuple(f "{x : .2f}" for x in res)
print(formated)