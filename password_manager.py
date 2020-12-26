
class PasswordManager(object):

    def __init__(self, identity, service, user, password, date):

        self.__identity = identity
        self.__service = service
        self.__user = user
        self.__password = password
        self.__date = date

    def __repr__(self):
        return f'Service: {self.__service}\nUser: {self.__user}\nPassword: {self.__password}'

    @property
    def identity(self):
        return self.__identity

    @property
    def service(self):
        return self.__service

    @service.setter
    def service(self, service):
        self.__service = service

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def date(self):
        return self.__date
