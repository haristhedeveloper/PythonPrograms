# In this program we know how to check the number is prime or not
# First prime is the number who is divisible by 1 and himself just


number=int(input("Enter any number : "))
if number>=5: #this condition check number is equal or greater than 5 bcz its have a little bit error if we give number less than 5
 number1=number-1 #in this condition we subtract 1 from the original number
 for i in range(2,number1): #this loop store the value from 2 to one less than original number
  if number % i == 0: #this check number is prime or not
    print("The number is not Prime")
    break
  else:
   print("The number is Prime")
   break
else: #if number less than 5 than this part of program is running
 if number==1 and 3:
  print("The number is Prime")
 else:
  print("The number is not Prime")