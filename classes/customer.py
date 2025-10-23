from classes.user import User


class Customer(User):
    
    def __init__(self, username: str, email: str, password: str, address: str):
        super().__init__( username, email, password)
        self.address = address


    def get_details(self):
        print(f"Пользователь: {self.username} с эл. адресом: {self.email} адрес доставки: {self.address}")
