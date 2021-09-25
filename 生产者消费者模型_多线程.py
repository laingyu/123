from threading import Thread
import time
cake = 500
price = 2

class Buyer(Thread):
    name = ""
    money = 3000
    num = 0
    def run(self) -> None:
        global cake,price
        while True:
            if cake == 0  and self.money >= 2:
                for i in range(2):
                    print(".",end="")
                    time.sleep(1)

            elif self.money > 2 and cake >0:
                cake = cake - 1
                self.num = self.num + 1
                self.money = self.money - price
                print("%s买了1个蛋挞!还剩%s￥。"% (self.name, self.money))
            else:
                print("%s一共买了%s个蛋挞!"% (self.name,self.num))
                break

    def GetMoney(self):return self.money

class Cook(Thread):
    name = ""
    num = 0
    def run(self) -> None:
        global cake
        while True:
            if cake == 500:
                for i in range(3):
                    print(".",end="")
                    time.sleep(1)
            elif cake < 500 :
                print("%s师傅加工完成了一个蛋挞!", self.name)
                cake = cake + 1
                self.num = self.num + 1
            else:
                print("%s师傅一共做了%s个蛋挞!"% (self.name ,self.num))
                break




a1 = Cook()
a1.name = "魏一"
a2 = Cook()
a2.name = "卜二"
a3 = Cook()
a3.name = "张三"

b1 = Buyer()
b1.name = "一一"
b2 = Buyer()
b1.name = "二哥"
b3 = Buyer()
b1.name = "小三"
b4 = Buyer()
b1.name = "四少"
b5 = Buyer()
b1.name = "小武"
b6 = Buyer()
b1.name = "六娃"

b1.start()
b2.start()
b3.start()
b4.start()
b5.start()
b6.start()
# if b1.GetMoney() > 2 or b2.GetMoney() > 2 or b3.GetMoney() >2 or b4.GetMoney() > 2 or b5.GetMoney() > 2or b6.GetMoney() >2:
a1.start()
a2.start()
a3.start()
