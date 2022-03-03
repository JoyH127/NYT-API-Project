data = [{
          "id": 1,
          "first_name": "Townsend",
          "last_name": "Dansken",
          "email": "tdansken0@yahoo.com",
          "subscribed": True
        }, {
          "id": 2,
          "first_name": "Mariejeanne",
          "last_name": "Edgar",
          "email": "medgar1@google.es",
          "subscribed": False
        }, {
          "id": 3,
          "first_name": "Sheila",
          "last_name": "McBeith",
          "email": "smcbeith2@bluehost.com",
          "subscribed": False
        }, {
          "id": 4,
          "first_name": "Duncan",
          "last_name": "Kull",
          "email": "dkull3@blinklist.com",
          "subscribed": True
        }, {
          "id": 5,
          "first_name": "Rodger",
          "last_name": "Lockhart",
          "email": "rlockhart4@about.com",
          "subscribed": False
        }]

# Start your code below this line.
# the code starts by setting the subscriber count to 0
# the code then adds +1 to the subs count for everyone that is a subscriber
# lists non sub names and put its next to special deal

"""
subs = 0
for dict in data:
    if dict['subscribed'] is True:
        subs += 1
print("There are currently %s people subsribed\n" % subs)

for dict in data:
    if dict['subscribed'] is False:
        print("Speical deal: %s %s, %s" % (dict['first_name'],
                                           dict['last_name'],
                                           dict['email']))
"""

# instead of separate the code into two for loop,
# I will use only one for loop and combine the code
# not to run similar loop code.

subs = 0
for dict in data:
    if dict['subscribed'] is True:
        subs += 1
    elif dict['subscribed'] is False:
        print("%s %s, %s" % (dict['first_name'],
                             dict['last_name'],
                             dict['email']))
    else:
        pass
print("There are currently %s people subsribed\n" % subs)

"""

# I changed fewer lines of code, erase else code.
# print style can use just "f" to simplify the code,

subs = 0
for dict in data:
    if dict['subscribed'] is True:
        subs += 1
    elif dict['subscribed'] is False:
        print("%s %s, %s" % (dict['first_name'],
                             dict['last_name'],
                             dict['email']))

print(f"There are currently {subs} people subsribed\n")

"""