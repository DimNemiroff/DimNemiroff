class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        print("A - call method __new__ for " + str(cls))
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            print("A1 - ", cls.__instance)
        return cls.__instance

    def __init__(self, user, pasw, port):
        print("B - call method __init__ for " + str(self))
        self.user = user
        self.pasw = pasw
        self.port = port

    def __del__(self):
        print("C - deletion " + str(self))
        DataBase.__instance = None

    def connect(self):
        print(f"connect to db {self.user}, {self.pasw}, {self.port} ")


db = DataBase('root', '1234', 80)
print("0", id(db))
db.connect()

'''print("1", Point)
print("2", Point())
print("25", pt)
print("3", pt.set_method)
print("35", pt.set_coord)
print("4", pt.set_method())
print("5", pt.set_coord(5, 7))
print("55", pt.get_coord())
print('6', pt.circle, pt.color, pt.__dict__)

Point.set_method("mgkhg")

print("7", pt)
print("8", pt.set_coord)
print("8", pt.set_coord())
pt.set_coord()
Point.set_coord(pt)
'''
