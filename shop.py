from classes.user import User
from classes.customer import Customer
from classes.admin import Admin
from classes.service import AuthenticationService

new_user = User('Vladimir', 'vreboot@yandex.ru', 'pass')
new_user.get_details()
new_user.register_new_user()

### check registration new user
print(User.users)


new_user.login()
new_user.logout()


second_user = Customer('Svetlana', 'sveta@yandex.ru', 'p@ssword', 'Stroiteley street, 12')
second_user.get_details()
second_user.register_new_user()
print(User.users)

second_user.login()
second_user.logout()




admin_user= Admin('boss', 'main@yandex.ru', 'Pa$$w0rd', 15)
admin_user.get_details()
admin_user.register_new_user()
admin_user.login()
print(User.users)
admin_user.list_users()
admin_user.delete_user('Vladimir')
admin_user.list_users()

print("-" * 30)

auth_service = AuthenticationService()
