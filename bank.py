import random
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、存钱              ------------|")
print("|------------3、取钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
class People(object):
    # 定义客户基本属性：客户名，账号，密码，国籍，所在地址(省份、街道、门牌号)，账户余额，开户行

    def __init__(self):
        self.name = ""
        self.account = ""
        self.password = ""
        self.country = ""
        self.province = ""
        self.street = ""
        self.door = ""
        self.money = 0
        self.bank_name = ""
dict = {
    88888888: {
        'password': '123456', 'name': '22', 'country': '22', 'province': '22', 'street': '22', 'door': '22', 'money':500, 'bank_name': '工行'
    },
    11111111:{
    'password': '123456', 'name': '22', 'country': '22', 'province': '22', 'street': '22', 'door': '22', 'money': 500,
    'bank_name': '工行'
    }

}

class Bank(object):

    def new_account(self):
        car = random.randint(10000000, 99999999)
        # s随机生成一个8位的账号
        return car

    # 添加用户
    def add_user(self):
        att = {}
        user_1 = People()
        user_1.name = input("请输入姓名：")
        user_1.country = input("国籍：\t")
        user_1.province = input("所在城市 ：")
        user_1.street = input("街道：\t")
        user_1.door = input("门牌号：\t")
        while True:
            user_1.password = input("请输入密码:")
            a = len(user_1.password)
            if a == 6:
                b = input("请确认密码:")
                if b == user_1.password:
                    att["password"] = user_1.password
                    break
                else:
                    print("两次密码不一致，请重新输入。")
                    continue
            else:
                print('密码长度为6位，正常输入。')
                continue
        att["name"] = user_1.name
        att["country"] = user_1.country
        att["province"] = user_1.province
        att["street"] = user_1.street
        att["door"] = user_1.door
        att["money"] = 0
        att["bank_name"] = "工行"
        c = Bank.new_account(self)
        if len(dict) > 100:
            print("开户失败，库累哭了。")
        else:
            if c in dict:
                print("开户失败，账号已存在。")
            else:
                user_1.account = c
                dict[c] = att
                print("开户成功，您的账号为%d"%c)

    # 存钱
    def save(self):
        car = int(input("请输入您的账号："))
        money = int(input("请输入您预存金额："))
        print(dict)
        if car not in dict.keys():
            print("False")
        else:
            print("您的账号余额为%s" % (dict[car]['money']))
            dict[car]["money"] = dict[car]["money"] + money
            print("储存成功!")
            info = '''
                      ---------账号信息------------
                      账号：%s
                      余额：￥%s
                      开户行：%s
            '''
            print(info % (car, dict[car]["money"], dict[car]["bank_name"]))

    # 取钱
    def draw(self):
        num = 1      # 定位错误输入密码次数，3次冻结账号
        car = int(input("请输入账号："))
        password = input("请输入密码：")
        if car not in dict.keys():
            print("False,账户错误。")
        else:
            while True:
                if num < 3:
                    if password != dict[car]["password"]:
                        password=input("密码错误，请重新输入密码：")
                        num += 1
                        continue
                    else:
                        while True:
                            print("您账号余额为%s" %(dict[car]["money"]))
                            money = int(input("输入取款金额："))
                            if money > dict[car]["money"]:
                                print("余额不足，重新输入。")
                                continue
                            else:
                                dict[car]["money"] = dict[car]["money"]-money
                                info = '''
                                          ---------账号信息------------
                                          账号：%s
                                          余额：￥%s
                                          开户行：%s
                                '''
                                print(info % (car, dict[car]["money"], dict[car]["bank_name"]))
                                break    # 跳出内循环，该循环用于判断所取金额大于余额
                        break  # 跳出外循环，该循环用于判断输入密码错误次数
                else:
                    print("连续三次密码输入错误，账户%s冻结24小时"%(car))
                    break

    # 转账
    def transfer(self):
        num = 1
        car1 = int(input("请输入付款人账户："))
        password = input("请付款账户密码：")
        if car1 not in dict.keys():
            print("False,账户错误。")
        else:
            while True:
                if num < 3:
                    if password != dict[car1]["password"]:
                        password = input("密码错误，重新输入：")
                        num += 1
                        continue
                    else:
                        car2 = int(input("请输入收款人账户："))
                        if car2 not in dict.keys():
                            print("False,账户错误。")
                        else:
                            money = int(input("请输入转账金额："))
                            if money > dict[car1]["money"]:
                                print("转那么多，您想吃土啊。")
                            else:
                                dict[car1]["money"] = dict[car1]["money"]-money
                                dict[car2]["money"] = dict[car2]["money"]+money
                                info = '''
                                          ---------账号信息------------
                                          账号：%s
                                          余额：￥%s
                                          开户行：%s
                                '''
                                print(info % (car1, dict[car1]["money"], dict[car1]["bank_name"]))
                        break

                else:
                    print("连续三次密码输入错误，账户%s冻结24小时" % (car1))
                    break
    # 查询
    def query(self):
        num = 1
        car = int(input("请输入账户："))
        password = input("请输入密码：")
        if car not in dict.keys():
            print("False,账户错误。")
        else:
            while True:
                if num >= 3:
                    print("连续三次密码输入错误，账户%s冻结24小时" % (car))
                    break
                else:
                    if password != dict[car]["password"]:
                        password = input("密码错误，重新输入：")
                        num += 1
                        continue
                    else:
                        info = '''
                        ---------账号信息 - -----------
                        账号： % s
                        余额：￥ % s
                        开户行： % s
                    '''
                    print(info % (car, dict[car]["money"], dict[car]["bank_name"]))
                    break

a = Bank()
while True:
    begin = input("请选择业务")
    if begin == "1":  # 您输入的业务等于1执行开户操作
        print(1, "、开户")
        a.add_user()
    elif begin == "2":
        a.save()
        print(2, "、存钱")
    elif begin == "3":
        print(3, "、取钱")
        a.draw()
    elif begin == "4":
        print(4, "、转账")
        a.transfer()
    elif begin == "5":
        print(5, "、查询")
        a.query()
    else:
        print(6, "、退出")
        break

