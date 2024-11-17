#"Imagine you are working on a project for an e-commerce website.
#  The website stores product ratings in a list for each product, 
# where customers can rate a product from 1 to 5. You need to develop 
# a feature that identifies the highest rating given to a particular product.

#For example, if a product has ratings 3 5 4 2 5 you need to identify the highest rating (which is 5) 
# so that you can highlight this on the product page.

#Input Format Description:
#The input consists of a list of integers.
#Each integer is separated by a space.
#The list can have any five number of elements (including duplicates).

#Test Cases:
#Test Case 1: 3 5 4 2 1
#Output: 5
#Explanation: The list contains multiple ratings, and the highest rating is 5.
numbers=list(map(int, input("Enter the List values: ").split()))
largest=numbers[0]
for i in range(1,len(numbers)):
    if (numbers[i]>largest):
        largest=numbers[i]
print(largest)