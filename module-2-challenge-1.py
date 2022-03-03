# Get the number from the user's input and assign the value as an integer value through "input()".
#  So, the input cannot get any differnt types of number except for integer. 
number = int(input('Type any number you want: '))

# If statement tests whether the number is odd or even through the remainder. 
# When a number is divided 2, the result 1 means odd. 
# Print() print the number and "," concatenate sentences and variable.
if number%2==1:
    print( "Your number is",number,"This number is odd")
else:
    print("Your number is",number,"This number is even")


