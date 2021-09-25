import time ,sys
class OldPhone(object):
    __brand = "华为"

    def setbrand(self,brand=__brand):
        self.__brand = brand
    def getbrand(self):
        return self.__brand
    def call(self,number):
        print("正在给%s打电话..."% number)
        for i in range(5):
            print(".",end="")
            time.sleep(1)
        print("")

class NewPhone(OldPhone):

    def call(self,number):
        print("语言拨号中....")
        for i in range(5):
            print(".", end="")
            time.sleep(1)
        print("")
        super().call(number)
    def show(self):
        print("%s品牌的手机很好用!"% super().getbrand())

a = NewPhone()
ifno = '''
--------------------
 1、 更换手机        +
 2、 拨号           +
 3、 查看当前手机     +
 4、 退出           +
--------------------
'''
print(ifno)
while True:
    choose = input("你要干啥：")
    if choose == "1":
        a.setbrand(input("更换手机："))
        a.show()
    elif choose == "2":
        a.call(input("拨号："))
    elif choose == "3":
        a.show()
    elif choose == "4":
        print("Bye!")
        sys.exit()
    else:
        print("别瞎输入!")
        continue
