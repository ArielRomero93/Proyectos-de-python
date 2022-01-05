def singleton(cls):

    instancias = dict()

    def wrap(*args, **kwargs):
        if cls not in instancias:
            instancias[cls] = cls(*args, **kwargs)

        return instancias[cls]

    return wrap


@singleton
class User(object):
    def __init__(self, username):
        self.username = username


if __name__ == '__main__':
    user1 = User('Ariel')
    user2 = User('Romero')

    print(user1 == user2)