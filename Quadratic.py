# Quadratic formula  -b±√(b²-4ac)/(2a)
# In this program we know how to calculate the value of quadratic formula

# First, we take three number as a input from the user
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))

# Then calculate this part √(b²-4ac) of the formula
root=(b**2-4*a*c)**0.5   #**0.5 is use for the square root

# Finally calculate the whole quadraic formula

forplus= (-b+root)/(2*a)
forneg= (-b-root)/(2*a)

print(forplus)
print(forneg)
