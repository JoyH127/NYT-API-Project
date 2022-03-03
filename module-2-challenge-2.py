# get a user input and assign it into an alphabet variable. \n is the new line, so it shows a more readable structure.
alphabet = input('Hi, I am an alphabet detector! \nType a letter you want!\n: ')

# len() shows the length of strings. If a user types one more letter, the value of it will be more than 1. So, ask to re-enter one letter.  
# This While loop will end when a user types only one letter and continues the first if condition.
while len(alphabet)>1:
    alphabet = input('Type One letter please!\n: ')

# The first if condition tests whether any vowel inputs like a,e, i,o,u. 
# If it is true,  it will take action to print the announcement about a vowel. 
# elif statement is another if statement that continues to check whether any inputs like y, Y.

if alphabet == 'a' or  alphabet == 'A' or alphabet == 'e' or alphabet == 'E' or alphabet == 'i' or  alphabet == 'I' or  alphabet == 'o' or  alphabet == 'O' or  alphabet == 'u' or alphabet == 'U':
   print("your entered letter is a vowel.")
elif alphabet == 'y' or alphabet =='Y': 
    print("\nY is a vowel, and sometimes y is a consonant.")        
else:
    print("your letter is consonant.")