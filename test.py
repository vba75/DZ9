data = [['user1', 'email1@example.com', 'pass1'],   
        ['user2', 'email2@example.com', 'pass2'],   
        ['user3', 'email3@example.com', 'pass3']]  
  


usernames = [item[0] for item in data]


print(usernames)


username = "user2"
result = [user for user in data if user[0] == username]

print(result)