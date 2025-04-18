# from enum import Enum
#
# class Colors(Enum):
#     BLACK = "black"
#     RED =  "red"
#     BLUE = "blue"
#
#
# class Enemy:
#     def __init__(self,name: str,color: Colors,type: str):
#         self.name = name
#         self.color = color
#         self.type = type
#
#
#
#
# black = "black"
# enemies = []
# enemies.append(Enemy("...", Colors.BLACK,"robot"))
# enemies.append(Enemy("...", Colors.BLACK,"robot"))
# enemies.append(Enemy("...", Colors.BLACK,"robot"))
# enemies.append(Enemy("...", Colors.BLACK,"robot"))
# enemies.append(Enemy("...", Colors.RED,"robot"))
# enemies.append(Enemy("...", Colors.RED,"player"))
# enemies.append(Enemy("...", Colors.RED,"player"))
# enemies.append(Enemy("...", Colors.BLUE,"player"))
# enemies.append(Enemy("...", Colors.RED,"player"))
# enemies.append(Enemy("...", Colors.RED,"player"))
# enemies.append(Enemy("...", Colors.RED,"player"))

class Singleton:
    def __new__(cls, *args, **kwargs):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = super().__new__(cls)
        it.init(*args, **kwargs)
        return it

    def init(self, *args, **kwargs):
        print(args, kwargs)

    def __init__(self, *args, **kwargs ):
        print("iiinit",args, kwargs)


s1 = Singleton("aaa", x="aaa")
s2 = Singleton("bbb")
print(id(s1))
print(id(s2))
