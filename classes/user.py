import hashlib
import uuid 


class User:
    users = []
    session =[]


    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = self.hash_password(password)
#        if self.check_unique_username(username) :
#            self.register_new_user(self.username, self.email, self.password)
#            self.login(self.username, self.password)
#        else:
#            print('Пользователь с таким именем зарегистрирован, придумайте другое')


    @staticmethod
    def hash_password(password: str):
        return hashlib.sha1(password.encode()).hexdigest()


    def check_password(self, stored_password: str, prvided_password: str):
        return stored_password == User.hash_password(prvided_password)


    def get_details(self):
        print(f"Пользователь: {self.username} с эл. адресом: {self.email} ")


    def check_unique_username(self, username: str)->bool: 
        usernames = [item[0] for item in User.users]
        return not ( username in usernames )


    def login(self):
        record = [user for user in User.users if user[0] == self.username ]
        if record[0][2] == self.password:
            User.session.append(self.username)
            print(f"session is {User.session}" )


    def logout(self, ):  
        if self.username in User.session:
            User.session.remove(self.username)
            print(f"session is {User.session}" )


#    def register_new_user(self, username: str, email: str, password: str):
    def  register_new_user(self):
        if self.check_unique_username(self.username):
            User.users.append([self.username, self.email, self.password])
        else:
            print('Пользователь с таким именем зарегистрирован, придумайте другое')


