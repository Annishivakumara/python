#print Number from 1  to 10 except 6

for i in range(1,11):
    if i == 6:
        continue
    print(i , end=' , ')