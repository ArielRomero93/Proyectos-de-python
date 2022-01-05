class User(object):

    __instance = None

    def __new__(cls):
        if User.__instance is None:
            print('Nueva y única instancia')
            User.__instance = object.__new__(cls)
        return User.__instance
    
    # def __init__(self, username):
    #     self.username = username

if __name__ == '__main__':
    
    user1 = User()
    user2 = User()

    # user1 = User('Ariel')
    # user2 = User('Romero')
    
    print(user1 == user2)