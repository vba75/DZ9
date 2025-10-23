from classes.user import User
import pprint


class Admin(User):
    
    def __init__(self,  username, email, password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level
        pass

    def get_details(self):
        print(f"Имя пользователя администратора: {self.username} , его адрес эл. почты {self.email}, уровень {self.admin_level}") 
     

    @staticmethod
    def list_users():
        print(User.users)
     

    @staticmethod
    def delete_user(username: str):
        i = 0
        for user in User.users:
            if username in user:
                del User.users[i]
                print(f"Пользователь {username} удален")
            else: 
                i+=1    






