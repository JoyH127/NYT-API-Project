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

# The data set I assigned is
# a mixture of the list and dictionary.
# tempary variable 'i' will traversal
# the whole data list, which has a sequence.
# To print the number of subscribers,
# set the count 0 outside of a loop.
# To access my data, variable dic is going
# to get a dictionary from the data list.
# Using "dic. items", key and value can access
# each section of contents in for loop.
# Test both condition keyword is 'subscribed,'and value
# is true to get subscribers.
# dic.get(key) can get True value and
# int() function turn Boolean True value into integer 1.
# count will accumulate the number.
# elif statement helps to get unsubscribers who have false value.
# count should call outside of the code as it shows the total amount.
count = 0
for i in data:
    dic = dict(i)
    for key, value in dic.items():
        if key == 'subscribed' and value == True:
            count = count+int(dic.get(key))
        elif value == False:
            print(f"{dic.get('first_name')} needs subscription")
print(f"{count} subscriptions")
