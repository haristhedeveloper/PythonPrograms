# Lists are used to store multiple values in one variable 
# Values are of different types


fruits=['apple','watermelon','guava','cherry']
types=['haris',22,True] # this list contain three types of data

print(fruits)
print(types)

# You can also change the value of list by indexing

fruits[1]='mango'
print(fruits)

# Also access the list item by its index
print(fruits[3])

# Add item in the list at end by append method

fruits.append('strawberry')
print(fruits)

# Add item in the specific position in the list by insert method
fruits.insert(0,'pineapple')
print(fruits)

# Extend method is used to combine two list
fruits.extend(types)
print(fruits)