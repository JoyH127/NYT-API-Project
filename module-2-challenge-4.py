
# Get an grade from User's input. I set "float()" to get decimal points of grade. If I didn't set it, the assigned value will be String value. 
grade = float(input("Hey! I am your letter grade converter. \n Type your grade, and I will show your letter grade.\n:"))

# A user inputs a number more than 100 or 0, the range detects whether it is a proper input to evaluate a letter grade. 
# Loop continues until getting a valid input.
# each if statement will check the range of the letter grade in this semester. 
while grade > 100 or grade < 0:
    grade = float(input("I think you got the wrong grade, Please Re-enter.\n:"))
if 90 <= grade <= 100:
    print("Wow! your grade will be A. Perfect!")
elif 87 <= grade < 90:
    effort = 90-grade
    print("your grade will be B+.")
    print("If you get" , effort , "points ,you can get A." )
    print ("Try it!, you are doing well!") 
elif 80 <= grade < 87:
    effort = 87-grade
    print("your grade will be B.")
    print("If you get" , effort , "points ,you can get B+." )
    print ("Try it!, you are doing well!") 
elif 77 <= grade < 80:
    effort = 80-grade
    print("your grade will be C+.")
    print("If you get" , effort , "points ,you can get B." )
    print ("Try it!, you can get better grade.") 
elif 70 <= grade < 77:
    effort = 77-grade
    print("your grade will be C.")
    print("If you get" , effort , "points ,you can get C+." )
    print ("Try it!, you can get better grade.") 
elif 60 <= grade < 70:
    effort = 70-grade
    print("your grade will be D.")
    print("If you get" , effort , "points ,you can get C." )
    print ("Try it!, you can pass the course.") 
else:
    effort = 60-grade
    print("your grade will be F.")
    print("If you get" , effort , "points ,you can get D." )
    print("You need to study hard! Don't give up till the end of semester.")
