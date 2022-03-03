# made a vowel list to test whether the alphabet has any vowels.
# it is one of the collection objects.
vowel = ["a","e","i","o","u"]

# get a user input and assign into alphabet variable.
# Also lower() function will help you change all strings.
# So, it doesn't need to include Capital letters in a vowel list.
alphabet = input('Hi, I am an alphabet detector! \nType a letter you want!\n: ').lower()

while len(alphabet)>1:
    alphabet = input('Type One letter please!\n: ')

# It is an instance of input validation to test the input type.
# isalpha is a string method to check whether it is String.
# The first if statement is also an instance of type testing.
if alphabet.isalpha():
    
    # This will be checked the alphabet variable has any
    # strings in a vowel list.
    if alphabet in vowel:
        print("your entered letter is a vowel.")
    # It doesn't need to 'Y' as all input will be lowercase.
    elif alphabet == 'y':
        print("\nY is a vowel, and sometimes y is a consonant.")        
    else:
        print("your letter is consonant.")
else: 
    print('Try again, RE-ENTER your alphabet. ')
