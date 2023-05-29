from services.mongo_service import list_games, delete_game, save_user, get_user 

#list_games()
#delete_game("646e5098ae64e7f3ca98fa52")
#print('-----------')
#list_games()

#save_user({"email":"ivilavitoria@gmail.com", "password": "test2023"})

user = get_user("ivilavitoria@gmail.com")
if user != None:
    print (user["email"])
    passwordStored = user["password"]
    passWord = "test2023" 
    if passWord == passwordStored:
        print ("Login Ok")
    else:
        print ("Incorrect Password")
else:
    print("User dont exists!")
