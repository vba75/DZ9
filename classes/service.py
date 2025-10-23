from classes.user import User
import hashlib


class AuthenticationService():
    
    # session =  []
    current_user: User
    
    def __init__(self):        
         self.session =  []

    def register(self, username: str, email: str, password: str, *args):
        
        current_user = User(username, email, password, args[0] )
        if current_user.check_unique_username(username):
            current_user.users.append([username, email, password, args[0]])
        else:
            print('Пользователь с таким именем зарегистрирован, придумайте другое')
        

    def login(self, username: str, password: str):
        record = [user for user in current_user.users if current_user[0] == username ]
        if record[0][2] == current_user.hash_password(password):
            self.session.append(username)
            print(f"session is {self.session}" )

    def logout(self):
        if current_user.username in self.session:
            self.session.remove(current_user.username)
            print(f"session is {self.session}" )

    def get_current_user(self):
        print(f"Текущий пользователь: {current_user.username} Адрес эл. почты: {current_user.email} ")
        
        

    
