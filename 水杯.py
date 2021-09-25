import sys
class Cup(object):
    __highly = 0.0
    __volume = 0.0
    __color =" "
    __texture = " "

    def work(self):
        print("这是一个可以装%sL水，高%scm%s%s的杯子"%(Cup.__volume,Cup.__highly,Cup.__color,Cup.__texture))

    def sethighly(self,highly=15):
        if highly <=0 or highly >100:
            print("高度错误，您的杯子牛逼炸了!")
            sys.exit()
        else:
            Cup.__highly = highly

    def setvolume(self, volume=0.55):
        if volume <= 0 or volume>100:
            print("容量错误，您的杯子牛逼炸了!")
            sys.exit()
        else:
            Cup.__volume = volume

    def setcolor(self, color="无色"):
        Cup.__color = color

    def settexture(self, texture="塑料"):
        Cup.__texture = texture

    def gethighly(self):
        return Cup.__highly

    def getvolume(self):
        return Cup.__volume

    def getcolor(self):
       return Cup.__color

    def gettexture(self):
        return Cup.__texture

class Computer(object):
    __size = 15.6        # 屏幕大小
    __cup = "Intel(R) Core(TM) i5-7300HQ CPU @ 2.50GHz   2.50 GHz"
    __price = 5000.0     # 价格
    __memory = 4         # 内存
    __work_time = 12     # 待机时长

    def setsize(self, size=__size):
        if size <= 0 or size > 100:
            print("屏幕大小错误，您的电脑牛逼炸了!")
            sys.exit()
        else:
            Computer.__size = size

    def setcpu(self, cpu=__cup):
        Computer.__cup=cpu

    def setprice(self, price=__price):
        if price <= 0 :
            print("不收冥币!")
            sys.exit()
        else:
            Computer.__price = price

    def setmemory (self, memory =__memory):
        if memory <= 0:
            print("阴间内存!")
            sys.exit()
        else:
            Computer.__memory = memory

    def setwork_time  (self,work_time =__work_time):
        if work_time  <= 0:
            print("阴间待机时长!")
            sys.exit()
        else:
            Computer.__work_time = work_time

    def getsize(self):
        return Computer.__size

    def getcpu(self):
        return Computer.__cup

    def getprice(self):
        return Computer.__price

    def getmemory(self):
        return Computer.__memory

    def getwork_time (self):
        return Computer.__work_time
    def typing(self):
        print("欢迎使用打字功能!")
    def game(self):
        print("欢迎来到游戏世界!")
    def video(self):
        print("欢迎登录少儿频道!")
    def pcshow(self):
        print("大小为%s寸，运行内存%sG，CPU型号%s可待机%s小时的笔记本电脑只卖%s￥"% (self.__size,self.__memory,self.__cup,self.__work_time,self.__price))




a = Cup()
# highly =input("请输入杯子高度：")
# volume = input("杯子容量：")
# if highly.isalpha() or volume.isalpha()  :    # 逆向思维，判断是否是字母
#     print("错误输入,别瞎搞!")                   # 是，提示错误，结束运行
#     sys.exit()
# else:
#     a.sethighly(float(highly))
#     a.setvolume(float(volume))
# a.setcolor(input("杯子颜色："))
# a.settexture(input("杯子材质："))
a.setvolume()
a.setcolor()
a.settexture()
a.sethighly()
a.work()

b = Computer()
b.setsize()
b.setmemory()
b.setcpu()
b.setprice()
b.setwork_time()
b.game()
b.video()
b.typing()
b.pcshow()