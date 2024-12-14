#Adding Items 
a=dict()
a[4]="Four" "nalaku"
a.update({5: 'five' })
print(a)

#modifying anfd getting elemenets in the dict using get key word
person=dict()

name=input("Enter The Nam: ")
age=int(input("Enter The age: "))
person['name']=name
person['age']=age
 
person['age']=31
print("names",person['name'])
print("Age",person['age'])
print(person.keys())
print(person.values())