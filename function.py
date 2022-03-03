'''
My function name is separate and gets an argument(sentence).
The string object will pass as a parameter into what.
The blank should assign to detect whether the argument has
space between words.
Each error message has to be assigned to return its value.
The first if statement has an isinstance()
which checks "what" is the string class.
The second blank checks the space in what(sentence).
Replace () detects comma and replace into nothing, so
it erases the comma in the sentence.
Lower () makes the sentence into lowercase.
The clean variable will be assigned to a new list made by
split(). Split() literally splits the sentence by spaces
and creates a list object.
each return saves a value, but the programmer
should use print if the programmer wants to see
the return value.
'''


def separate(sentence):
    what = sentence
    blank = " "
    error1 = "You don't have any spaces."
    error = "Please, type any sentence."
    if isinstance(what, str):
        if blank in what:
            what = what.replace(',', "")
            what = what.lower()
            clean = what.split()
            return clean
        else:
            return error1
    else:
        return error

print(separate("Hello, This is the World. PLE,ASE FOLL,OW INST,AGRAM"))
