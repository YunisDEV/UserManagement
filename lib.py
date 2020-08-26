class User:
    def __init__(self, _name, _surname, _username, _password):
        self.name = _name
        self.surname = _surname
        self.username = _username
        self.password = _password

    def showData(self):
        print(f"{self.name} | {self.surname} | {self.username} | {self.password}")
