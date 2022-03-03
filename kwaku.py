def splicer (cut):
  a = cut.replace(',',"")
  return a

user = input('Please enter your sentence: ')
'''
The user will enter
a string and it will
be split into commas
and returned as a list
'''
try:
    float(user)
    print('There should be no numbers here. ')

except ValueError:
  ask_user = input('Would you like to strip \
  commas? Yes or No? ').lower()
  ask_user = splicer(ask_user)  
  
  if ask_user == 'yes':
     x = ask_user.split()
     print(x)

  elif ask_user == 'no':
    x = ask_user.split()
    print(x)

