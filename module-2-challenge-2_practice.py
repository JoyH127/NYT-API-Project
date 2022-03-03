# get a user input and assign into alphabet variable.
alphabet = input('Hi, I am an alphabet detector! \nType a letter you want!\n: ')


if isinstance(alphabet,(string)): 

    #  The first condition test checks whether any vowel input like a,e,i,o,u. 
    if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u':
        print("your entered letter is a vowel.")
    # why elif alphabet == 'y' or alphabet =='Y' doesn't work? 
    elif alphabet in('y','Y'):
        print("\nY is a vowel, and sometimes y is a consonant.")        
    else:
        print("your letter is consonant.")
else: alphabet = input('Try again, RE-ENTER your alphabet. ')