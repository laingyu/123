import random
import sys
import time
import pymysql
# 连接
con = pymysql.connect(host="localhost", user="root", password="root", database="工行管理系统")
# 创建控制台
cursor = con.cursor()


def information(data):  # 打印账户信息
    print("加载中......")
    time.sleep(3)
    info = '''
                                             ---------%s的账号信息------------
                                             账号：%s
                                             余额：￥%s
                                             开户行：%s
                                   '''
    print(info % (data[0][1], data[0][0], data[0][7], data[0][9]))
    time.sleep(3)


class Bank(object):
    def show(self):      # 显示可操作得业务类型
        print("==============================================")
        print("|------------中国工商银行账户管理系统-------------|")
        print("|------------1、开户              ------------|")
        print("|------------2、存钱              ------------|")
        print("|------------3、取钱              ------------|")
        print("|------------4、转账              ------------|")
        print("|------------5、查询              ------------|")
        print("|------------6、退出              ------------|")
        print("==============================================")

    def new_account(self):        # 随机生成一个8位的账号
        car = str(random.randint(10000000, 99999999))
        return car

    # 添加用户
    def add_user(self):
        # 申请账号的基本信息
        name = input("请输入姓名：")
        country = input("国籍：\t")
        province = input("所在城市 ：")
        street = input("街道：\t")
        door = input("门牌号：\t")
        # 判断密码的正确性 ：
        #               1、密码必须由6位字符组成
        #               2、两次输入的密码是否一致
        while True:
            password = input("请输入密码:")
            if len(password) == 6:
                b = input("请确认密码:")
                if b == password:
                    break
                else:
                    print("两次密码不一致，请重新输入。")
                    continue
            else:
                print('密码长度为6位，正常输入。')
                continue

        c = Bank.new_account(self)           # 随机成功一个8位的账号

        sql = "select count(*) from bank;"   # 准备SQL语句：累加数据库的数据条数
        cursor.execute(sql)                  # 执行SQL语句
        data = cursor.fetchall()             # 提取数据库数据：用于判断
        if len(data) >= 100:                 # 判断数据库是否满了
            print("开户失败，库累哭了")

        sql1 = "select * from bank where account=%s;"       # 准备SQL语句：查询数据库是否存在c账号
        parm = [c]
        cursor.execute(sql1, parm)           # 执行SQL语句
        data = cursor.fetchall()             # 提取数据库数据

        if len(data) != 0:                  # date长度>0,说明查询出c账号，数据库已存在
            print("开户失败，账号已存在")

        else:
            sql2 = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"   # 准备SQL语句：新增
            parm1 = [c, name, password, country, province, street, door, 0, "工行"]

            cursor.execute(sql2, parm1)  # 执行SQL语句
            con.commit()                 # 提交数据：将缓存区的数据提交到MySQL中
            print("开户成功，您的账号为%s" % c)

    # 存钱
    def save(self):
        car = input("请输入您的账号：")
        money = int(input("请输入您预存金额："))

        sql = "select * from bank where account=%s"
        pram = [car]
        cursor.execute(sql, pram)
        date = cursor.fetchall()

        if len(date) > 0:                 # date长度大于0，表明数据库存在该账号
            money = money+date[0][7]      # 原有金额+存入金额

            sql1 = "update bank set money=%s where account=%s"   # 修改数据并提交
            pram1 = [money, car]
            cursor.execute(sql1, pram1)
            con.commit()

            cursor.execute(sql, pram)     # 重新查询，获取最新的数据信息并打印
            date1 = cursor.fetchall()
            print("储存成功!")
            information(date1)
        else:
            print("账号不存在。")

    # 取钱
    def draw(self):
        num = 1                       # 定位错误输入密码次数，3次冻结账号
        car = input("请输入账号：")
        password = input("请输入密码：")

        sql = "select * from bank where account=%s"
        pram = [car]
        cursor.execute(sql, pram)
        date = cursor.fetchall()

        if len(date) > 0:
            while 1:
                if num < 3 and password != date[0][2]:
                    password = input("密码错误，请重新输入：")
                    num = num + 1
                    continue

                elif num >= 3 and password != date[0][2]:
                    print('连续3次密码错误，冻结该账户24小时。')
                    print('')
                    break

                else:
                    print("您账号可取金额%s元" % date[0][7])
                    money = int(input("预取金额："))
                    if money > date[0][7]:
                        print("余额不足。")
                        break

                    elif money <= 0:
                        print("错误金额。")
                        break

                    else:
                        money = date[0][7]-money

                        sql1 = "update bank set money=%s where account=%s"
                        pram1 = [money, car]
                        cursor.execute(sql1, pram1)
                        con.commit()

                        cursor.execute(sql, pram)
                        date1 = cursor.fetchall()
                        information(date1)
                        break
        else:
            print("账号不存在。")

    # 转账
    def transfer(self):
        num = 1
        car1 = input("付款人账户：")
        password = input("付款账户密码：")

        sql = "select * from bank where account=%s"
        pram = [car1]
        cursor.execute(sql, pram)
        date = cursor.fetchall()

        if len(date) > 0:
            while 1:
                if num < 3 and password != date[0][2]:
                    password = input("密码错误，请重新输入：")
                    num = num + 1
                    continue

                elif num >= 3 and password != date[0][2]:
                    print('连续3次密码错误，冻结该账户24小时。')
                    print('')
                    break

                else:
                    car2 = int(input("收款账号："))

                    pra2 = [car2]
                    cursor.execute(sql, pra2)
                    date1 = cursor.fetchall()

                    if len(date1) > 0:

                        money = int(input("转账金额："))
                        if money > date[0][7]:
                            print("余额不足。")
                            break

                        elif money <= 0:
                            print("错误金额。")

                        else:
                            money1 = date[0][7]-money             # 工行账号余额互转算法
                            money2 = date1[0][7]+money

                            sql1 = "update bank set money=%s where account=%s"   # 准备修改数据的SQL语句

                            pram3 = [money1, car1]                # 付款账号余额变更
                            cursor.execute(sql1, pram3)

                            pram4 = [money2, car2]                # 收款账号余额变更
                            cursor.execute(sql1, pram4)

                            con.commit()                           # 提交数据

                            cursor.execute(sql, pram)             # 重新查询修改后的付款账号信息，以用于打印
                            date2 = cursor.fetchall()

                            print("操作成功。")
                            information(date2)                    # 调用账号打印信息函数
                            break
                    else:
                        print("收款账号不存在。")
                        break

        else:
            print("账户不存在。")

    # 查询
    def query(self):
        num = 1
        car = input("请输入账户：")
        password = input("请输入密码：")
        sql = "select * from bank where account=%s"
        parm = [car]
        cursor.execute(sql, parm)
        # 提取数据
        date = cursor.fetchall()
        if len(date) > 0:
            while 1:
                if num < 3 and password != date[0][2]:
                    password = input("密码错误，请重新输入：")
                    num = num + 1
                    continue

                elif num >= 3 and password != date[0][2]:
                    print('连续3次密码错误，冻结该账户24小时。')
                    print('')
                    break

                else:
                    print("操作成功。")
                    information(date)
                    break
        else:
            print("账号不存在。")


a = Bank()
print("等待中.....")
time.sleep(3)
a.show()
while True:
    begin = input("请选择业务")
    if begin == "1":  # 您输入的业务等于1执行开户操作
        print(1, "、开户")
        a.add_user()
    elif begin == "2":
        print(2, "、存钱")
        a.save()
    elif begin == "3":
        print(3, "、取钱")
        a.draw()
    elif begin == "4":
        print(4, "、转账")
        a.transfer()
    elif begin == "5":
        print(5, "、查询")
        a.query()
    elif begin == "6" :
        print(6, "、退出")
        cursor.close()
        con.close()
        sys.exit()
    else:
        begin = input("没有该业务服务,请收重新选择：")
        continue
