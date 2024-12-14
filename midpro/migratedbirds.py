#times = int(input())#6
'''
bird_type = list(map(int,input().split()))
#1 4 4 4 5 3


bird_occurence = {}#suppose 1
most_frequent_bird = []

for i in bird_type:
    if i in bird_occurence:
        bird_occurence[i]=bird_occurence[i]+1
    else:
        bird_occurence.update({i:1})
max_frequency = max(bird_occurence.values())
 
for bird,count in bird_occurence.items():
        if count==max_frequency:
            most_frequent_bird.append(bird)
print(min(most_frequent_bird))
'''
times=int(input())
bird_type=list(map(int,input("Enter The List's: ").split()))

bird_ocurence={}
most_frequence=[]

for i in bird_type:
    if i in bird_ocurence:
        bird_ocurence[i]=bird_ocurence[i]+1
    else:
        bird_ocurence.update({i:1})
max_frequence=(max(bird_ocurence.values()))
for bird,count in bird_ocurence.items():
    if count==max_frequence:
        most_frequence.append(bird)
print(min(most_frequence))