class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print("deletion " + str(self))
    def set_method(self):
        print("call method 'set_method' " + str(self))

    def set_coord(self, x, y):
        print(self)
        self.x = x
        self.y = y

    def get_coord(self):
        return (self.x, self.y)


pt = Point()
print("1", Point)
print("2", Point())
print("25", pt)
print("3", pt.set_method)
print("35", pt.set_coord)
print("4", pt.set_method())
print("5", pt.set_coord(5, 7))
print("55", pt.get_coord())
print('6', pt.circle, pt.color, pt.__dict__)

Point.set_method("mgkhg")
'''
print("7", pt)
print("8", pt.set_coord)
print("8", pt.set_coord())
pt.set_coord()
Point.set_coord(pt)
'''
