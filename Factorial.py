
# It use to take input from the user
number=int(input("Enter the number :"))

fact=1

# It will iterate from 1 to number which is givenby the user
for i in range(1,number+1):
    fact=fact*i   # This line multiply 1 with every number in the loop and add

print(fact)


