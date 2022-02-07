class Member:
    def __init__(self, name, userName, password):
        self.__name = name
        self.__userName = userName
        self.__password = password

    @property
    def name(self):
        return self.__name

    @property
    def userName(self):
        return self.__userName

    @property
    def password(self):
        return self.__password

    @name.setter
    def name(self, name):
        self.__name = name

    @userName.setter
    def userName(self, userName):
        self.__userName = userName

    @password.setter
    def password(self, password):
        self.__password = password
