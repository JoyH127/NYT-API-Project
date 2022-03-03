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
"""
# Start your code below this line.
# This code will count the number of subscribers and display
# report of non subscribers
# Variables for number of people subscribed and
# list of nonsubscribers and their information
count = 0
nonsubscribers = []
# The loop to go through all the customers in the data given
for customer in data:
    # If the customer is subscribed increase the count by 1
    if customer.get("subscribed"):
        count = count+1
    # If the customer is not subscribed get their id, first
    # name, and last name and append it to the list of
    # nonsubscribers
    else:
        nonsubscribers.append((customer.get("id"),
                               customer.get("first_name"),
                               customer.get("last_name")))
# Display a report of the amount of people who are subscribed
# to email announcements.
print(f'There are {count} people subscribed for the email announcements.')
print(f'These people are to be offered a special deal:\n{nonsubscribers}')
"""
"""

Review: Her/His code look clean and used the list well.
The reason why save the unsubscribers' data in the new list is
not to print only the result. Outside the loop condition, 
it can print only one human-friendly message. Inside of the loop condition,
it can print the repeated same message. Also, if it doesn't use the list append, 
it is impossible to update the data. Amazing works. 

# Instead of using the list. I access variables directly 
# and print it out right away. I didn't save extra storage
# to print the list variable.

count = 0
for customer in data:
    if customer.get("subscribed"):
        count = count+1
    else:
        print(f"{customer.get('id')},{customer.get('first_name')},{customer.get('last_name')}")

print(f'There are {count} people subscribed for the email announcements.')

"""

# Like before, I did not use the get method and any other object collection.
# just print the unsubscribers list first,then print the original data

count = 0
print("Unsubcribers:")
for customer in data:
    if customer['subscribed']:
        count += 1      
    else: 
        print(f"{customer['first_name']},{customer['last_name']},{customer['email']}")

print(f'There are {count} people subscribed for the email announcements.')
