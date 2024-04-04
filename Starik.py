# In this program we know how to print starik from one to five with for loop
# Now we need two loops one for rows and other for the starik



for i in range(0,5):  # This loop print a row
    for j in range(0,i+1): #This loop print a starik
        print("*",end=' ')
    print("\r")

