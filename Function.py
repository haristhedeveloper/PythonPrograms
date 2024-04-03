# In this program we know about the functins 
# Function can be defined by using keyword "def"
# Function is used for reusability we call function at multiple places

def message(name): # name in the brackets is called arguments it is more than one
 print("Welcome in the class of Big Data Analytics Mr ",name)

message("haris")
message("furqan")
message("sohaib")
message("saeed")
message("adeel")
message("arslan")
message("rizwan")

# In the above program we use one welcome message for multiple persons this is called function reusability
 

# We use  " * "  this keyword with the function arguments when we don't know the numbers of arguments 
def childs(*kids):
 print( kids)

childs("haris","furqan")

# This method is use when we take input from the user
names=str(input("enter your kids names: "))
childs(names)