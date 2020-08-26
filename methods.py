from database import db
from lib import User


def getData():
    user_inputs = ['Name', 'Surname', 'Username', 'Password']
    return [input(uin+": ") for uin in user_inputs]


def createUser():
    return User(*getData())


def addToDb():
    db.append(createUser())


def showAll():
    for u in db:
        u.showData()


def showUserByName(name):
    for u in db:
        if u.name == name:
            u.showData()
            break


def getUserWithLongestName():
    user = None
    for u in db:
        if not user or len(user.name) < len(u.name):
            user = u


def getUserWithPassLongerThan(length):
    for u in db:
        if len(u.password) > length:
            u.showData()


def start():
    print('Type 1 to add users')
    print('Type 2 to show users')
    print('Type 3 to show user by name')
    print('Type 4 to show users that have password longer than 8')
    print('Type 5 to show user with longest name')
    print('Type 6 to exit')
    while True:
        cmd = input('enter command>> ')
        if cmd == "1":
            count = input('Enter count of users you want add: ')
            for i in range(int(count)):
                print(f"Add user no.{i+1}")
                addToDb()
        elif cmd == "2":
            showAll()
        elif cmd == "3":
            _name = input('Enter name: ')
            showUserByName(_name)
        elif cmd == "4":
            getUserWithPassLongerThan(8)
        elif cmd == "5":
            getUserWithLongestName()
        elif cmd == "6":
            break
        else:
            pass
