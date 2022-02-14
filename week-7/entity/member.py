class Member:
    def __init__(self, id=None, name=None, userName=None, password=None):
        self.__id = id
        self.__name = name
        self.__userName = userName
        self.__password = password

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def userName(self):
        return self.__userName

    @property
    def password(self):
        return self.__password

    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    @userName.setter
    def userName(self, userName):
        self.__userName = userName

    @password.setter
    def password(self, password):
        self.__password = password
