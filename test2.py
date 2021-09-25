import sys
import unittest


class Cook0(object):
    __name = ""
    __age = 0

    def SetName(self,name="张三"):
        self.__name = name
    def GetName(self):return self.__name
    def SetAge(self,age=30):
        if age > 0 and age <= 15:
            print("使用童工，你玩完了!")
            sys.exit()
        elif age >= 60:
            print("老人家已经退休啦!")
            sys.exit()
        elif age <= 0 :
            print("好家伙，整个阴间玩意!")
            sys.exit()
        else:
            self.__age = age
    def GetAeg(self):return self.__age
    def Steam(self):
        print("%s师傅正在蒸饭..."% self.__name)

class Cook1(Cook0):
    def Steam(self):
        print("今年%s岁的"% super().GetAeg(),end="" )
        super().Steam()

    def Stir(self):
        print("%s师傅正在炒菜..."% super().GetName())

class TestChef(unittest.TestCase):
    pass

class Cook3(Cook1):
    def Steam(self):
        super(Cook3, self).Steam()
    def Stir(self):
        super().Stir()

a = Cook3()
a.SetName(input("师傅姓名："))
a.SetAge(int(input("年龄：")))
a.Steam()
a.Steam()
a.Stir()