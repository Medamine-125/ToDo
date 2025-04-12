from peewee import *
from datetime import datetime
import os

db = SqliteDatabase('todo.db')
class Task(Model):
    title = CharField(max_length=100,
    null=False, unique=True)
    description = TextField(null=True)
    due_date = DateField(formats='%Y-%m-%d')
    status = BooleanField(default=False)

    class Meta:
        database = db





#Create a menu
def menu():
    print('\n')
    print("*********Menu**********")
    print("a/ ", add_user.__doc__)
    print("f/ ", find_user.__doc__ )
    print("d/ ", delete_user.__doc__)
    print("l/ ",list_users.__doc__ )
    print("q/ - Quit")

def add_user(first_name, last_name):
    """ Add a new user to database """
    User.create(first_name=first_name, last_name=last_name)
    print('User added successfully')

def find_user(last_name):
    """ Find a user """
    user_found = User.get_or_none(User.last_name==last_name)
    if user_found == None:
        print('Sorry, user not found')
    else:
        print(
        user_found.first_name,
        '----',
        user_found.last_name,
        '----',
        user_found.join_date)

def delete_user(user_id):
    """ Remove a user from database """
    user_to_be_deleted = User.get_by_id(user_id)
    user_to_be_deleted.delete_instance()
    print("User deleted succesfully...")

def list_users():
    """List all users"""
    # select all users from users table
    users =  User.select()
    for user in users:
        print(user.id, '|', user.first_name, '|', user.last_name, '|', user.join_date)






class User(Model):
    first_name = CharField(max_length=50, null=False, unique=False)
    last_name = CharField(max_length=50, null=True, unique=False)
    join_date = DateTimeField(formats='%Y-%m-%d %H:%M:%S', default=datetime.now)
    
    class Meta:
        database = db



if __name__ == '__main__' :
    #db.connect()
    #db.create_tables([Task, User])
    # Launch the menu at app startup
    #menu()
    
    while True: #always executed
        menu()
        choice = input('Enter your choice : ')
        if choice.lower() == 'q':
            break # stop the app
        elif choice.lower() == 'a':
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')  # Ensure correct naming
            add_user(first_name, last_name)
        elif choice.lower() == 'l':
            list_users()
        elif choice.lower() == 'd':
            os.system('cls')
            list_users()
            id = int(input('Give me the user id to delete it :  '))
            delete_user(id)
            list_users()
        elif choice.lower() == 'f':
            last_name = input('Enter the last name of the user : ')
            find_user(last_name)
