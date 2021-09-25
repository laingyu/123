import sys
class Air(object):
    __brand = "格力"
    __price = 4500.0
    __time = 30

    def setbrand(self, brand =__brand):
        self.__brand=brand
    def getbrand(self):return self.__brand
    def setprice(self,price=__price):
        if price <= 0:
            print("错误价格!不能小于等于0!")
            sys.exit()
        else:
            self.__price = price
    def getprince(self):return self.__price
    def settime(self,time=__time):
        if time < 0:
            print("时间不能小于零!")
        else:
            self.__time=time
    def gettime(self):return self.__time

    def open(self):
        print("空调开机了...")
    def  shutdowd(self):
        print("空调将在%s分钟后自动关机"% self.__time )
    def show(self):
        print("%s空调售价%s￥"% (self.__brand,self.__price))

a = Air()
ifno = '''
--------------------
+ 1、 开机           +
+ 2、 定时           +
+ 3、 更换空调        +
+ 4、 显示当选空调     +
+ 5、 退出           +
--------------------
'''
print(ifno)
while True:
    choose = input("请选择功能：")
    if choose=="1":
        a.open()
    elif choose=="2":
        a.settime(float(input("定时关机：")))
        a.shutdowd()
    elif choose=="3":
        a.setbrand(input("空调品牌："))
        a.setprice(float(input("空调价格：")))
        a.show()
    elif choose=="4":
        a.show()
    elif choose=="5":
        print("Bye")
        sys.exit()
    else:
        print("别瞎输入!")
