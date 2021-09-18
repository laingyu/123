import xlrd
#打开工作簿
wb = xlrd.open_workbook(r"C:\Users\11711\Desktop\python基础课\day7\2020年每个月的销售情况.xlsx")

class shop (object):
    def all_sum (self):            # 年销售总额
        sum = 0
        for i in range(0,12):
            # 确定选项卡
            sheet = wb.sheet_by_index(i)
            # 读取行与列
            row = sheet.nrows   # 行
            # col = sheet.ncols   # 列

            for j in range(1,row):
                data = sheet.row_values(j)
                sum =sum + data[2]*data[4]
        return sum

    def species(self,start=0,stop=12):   #  获取衣服种类
        name = []
        for i in range(start,stop):
            sheet = wb.sheet_by_index(i)
            row = sheet.nrows
            for j in range(1,row):
                data = sheet.row_values(j)
                name.append(data[1])
        name=set(name)
        name=list(name)
        return name

    def zhanbi(self,start=0,stop=12):           # 占比
        name = shop.species(self,start=start,stop=stop)               # 获取衣服种类
        num = [0]*len(name)                     # 存储对应衣服的数量
        money = [0]*len(name)                   # 存储对应衣服的销售金额
        sum_num = 0
        sum_money = shop.all_sum(self)

        for i in range(start,stop):
            sheet = wb.sheet_by_index(i)
            row = sheet.nrows

            for j in range(1,row):
                data = sheet.row_values(j)
                sum_num = sum_num + data[4]

                for x in range(len(name)):
                    if data[1]==name[x]:
                        num[x]=num[x]+data[4]
                        money[x]=money[0]+data[2]*data[4]

        # for y in range(len(name)):
        #     print("%s今年卖%s件，收入%s元"% (name[y], int(num[y]), round(money[y],2)))
        #     print("销售（件数）占:%s  销售（金额）占：%s"% ('{:.2%}'.format(num[y]/sum), '{:.2%}'.format(money[y]/sum1)))
        #     print("")

        return name, num, money ,sum_num ,sum_money

    def yue_zhanbi(self):              # 每个月每个类型衣服的月销售额占比
        for month in range(0,12):
            name,num,money,sum_num,sum_moeny = shop.zhanbi(self,start=month ,stop=month+1 )
            for i in range(len(name)):
                print("%s卖了%s元，销售额占%s月份总销售额的%s"% (name[i], round(money[i], 2), month+1, '{:.2%}'.format(money[i]/sum_moeny)))
            print("")
        return 0

    def max(self,quarter=5,moder="max"):
        if moder=="max":
            if quarter == 1:  # 第一季度 2、3、4
                name ,num ,money,sum,sum1 = shop.zhanbi(self,start=2-1,stop=4)

            elif quarter == 2:  # 第二季度 5、6、7
                name, num, money, sum, sum1 = shop.zhanbi(self, start=5-1, stop=7)

            elif quarter == 3:  # 第三季度 8、9、10
                name = shop.species(self)  # 获取衣服种类
                num = [0] * len(name)  # 存储对应衣服的数量

                for i in range(7, 10):
                    name, num, money, sum, sum1 = shop.zhanbi(self, start=8-1, stop=10)

            elif quarter == 4:  # 第四季度 11、12、1月份
                name = []
                month = ["1月","11月","12月"]
                for i in range(len(month)):
                    sheet = wb.sheet_by_name(month[i])
                    row = sheet.nrows

                    for j in range(1,row):
                        data = sheet.row_values(j)
                        name.append(data[1])

                name = set(name)
                name = list(name)
                num = [0]*len(name)
                for x in range(len(month)):
                    sheet = wb.sheet_by_name(month[x])
                    row = sheet.nrows

                    for j in range(1, row):
                        data = sheet.row_values(j)

                        for y in range(len(name)):
                            if data[1] == name[y]:
                                num[y] = num[y] + data[4]

            elif quarter == 5:  # 全年
                name ,num ,money,sum,sum1 = shop.zhanbi(self)
            else:
                print("请正确输入1——4季度。")
                return 0

            max = 0
            for i in range(len(num)):
                if num[max] >= num[i]:
                    max = max
                else:
                    max = i
            if quarter == 5:
                print("全年最畅销的衣服是%s,卖出了%s件" % (name[max], int(num[max])))
            else:
                print("第%s季度最畅销的衣服是%s,卖出了%s件" % (quarter, name[max], int(num[max])))

        elif moder=="min":
            name = shop.species(self)  # 获取衣服种类
            num = [0] * len(name)  # 存储对应衣服的数量

            for i in range(0, 12):
                sheet = wb.sheet_by_index(i)
                row = sheet.nrows

                for j in range(1, row):
                    data = sheet.row_values(j)

                    for x in range(len(name)):
                        if data[1] == name[x]:
                            num[x] = num[x] + data[4]
            min = 0
            for i in range(len(num)):
                if num[min] < num[i]:
                    min = min
                else:
                    min = i
            print("全年销量最低的衣服是%s,卖出了%s件" % (name[min], int(num[min])))

        else:
            print("仅仅提供季度畅销查询和年销售最低查询。")
            return 0
    def show(self):
        info = '''
*************服装商城管理系统功能选项卡************
*--------- 1、年销售额查询            ---------*
*--------- 2、服装年销售占比分析查询    ---------*
*--------- 3、服装月销售占比分析查询    ---------*
*--------- 4、最畅销与销售最低服装查询  ---------*
*--------- 5、重新打印功能卡          ---------*
*--------- 6、退出                  ---------*
*********************************************
             '''
        print(info)

a = shop()
a.show()
while True:
    choose = input("速度七十迈心情自由自在，请选择：")
    if choose == "1":
        sum=a.all_sum()      # 年销售额查询
        print("年销售额%s"% round(sum,2))
    elif choose == "2":
        name, num, money,sum,sum1 = a.zhanbi()          # 每种衣服年销售占比分析查询（销售量占比、销售额占比）
        for y in range(len(name)):
            print("%s今年卖%s件，收入%s元" % (name[y], int(num[y]), round(money[y], 2)))
            print("销售（件数）占:%s  销售（金额）占：%s" % ('{:.2%}'.format(num[y] / sum), '{:.2%}'.format(money[y] / sum1)))
            print("")
    elif choose == "3":
        a.yue_zhanbi()            # 每种衣服月销售占比查询
    elif choose == "4":
        y = input("季度查询输入1，年度查询输入2 :")    # 年、季度最畅销衣服查询和年最不景气的衣服查询
        if y.isdecimal():
            if y == "1":
                # for x in range(1,5):
                a.max(quarter=1)
                a.max(quarter=2)
                a.max(quarter=3)
                a.max(quarter=4)
                # x = input("自由自在的造，输入需要查询的季度：")
                # if x.isdecimal() and (x=="1" or x=="2"or x=="3" or x=="4"):
                #     x = int(x)
                # else:
                #     print("瞎输入，一边玩泥巴去。")
            elif y == "2":
                a.max()
                a.max(moder="min")
            else:
                print("瞎输入，一边玩泥巴去。")
        else:
            print("瞎输入，一边玩泥巴去。")
            continue
    elif choose == "5":
        a.show()
    elif choose == "6":
        print("Bye!")
        break
    else:
        print("今天星期三，上班呢，别瞎搞。")

