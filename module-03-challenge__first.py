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
count = 0
for i in data:
    for key in i:
        if key == 'subscribed' and i[key]==True:
            count = count + 1
        elif i[key] == False:
            for key in i:
                if key == 'first_name':
                    print(f"{i[key]} needs subscription for some special offer!")


print(f"{count} people are already subscibed.")  
            
        
        

          
    
  


       
         