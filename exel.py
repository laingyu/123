import xlrd
#打开工作簿
wb = xlrd.open_workbook(r"C:\Users\11711\Desktop\python基础课\day7\2020年每个月的销售情况.xlsx")

class shop (object):
    def all_sum (self,start=0, stop=12):            # 【start，stop）表中的销售总额
        sum = 0
        for i in range(start,stop):
            # 确定选项卡
            sheet = wb.sheet_by_index(i)
            # 读取行与列
            row = sheet.nrows   # 行
            # col = sheet.ncols   # 列

            for j in range(1,row):               # 累加销售额
                data = sheet.row_values(j)
                sum =sum + data[2]*data[4]
        return sum                               # 返回销售额

    def species(self,start=0,stop=12):   #  获取衣服种类
        name = []
        for i in range(start,stop):      # 获取【start，stop）表中的所有服装名称，存到neme列表中
            sheet = wb.sheet_by_index(i)
            row = sheet.nrows
            for j in range(1,row):
                data = sheet.row_values(j)
                name.append(data[1])
        name=set(name)                 # 对列表name进行去重处理
        name=list(name)
        return name                    # 返回服装名称列表

    def zhanbi(self,start=0,stop=12):           # 占比分析方法，参数“start=0,stop=12”默认是全年的分析，可具体到某某月的分析
        name = shop.species(self,start=start,stop=stop)               # 获取衣服种类
        num = [0]*len(name)                     # 销售数据列表，存储对应衣服的数量且与服装名称对应关系
        money = [0]*len(name)                   # 单种服装销售金额列表，存储与服装名称对应的销售金额
        sum_num = 0                             # 总销售数量
        sum_money = shop.all_sum(self,start=start,stop=stop)          # 销售总金额

        for i in range(start,stop):             # 根据参数start、stop获取【start，stop）表信息，获取表数据
            sheet = wb.sheet_by_index(i)
            row = sheet.nrows

            for j in range(1,row):
                data = sheet.row_values(j)
                sum_num = sum_num + data[4]     # 累计销售总数量

                for x in range(len(name)):
                    if data[1]==name[x]:
                        num[x]=num[x]+data[4]  # 累计单种服装销售数量
                        money[x]=money[0]+data[2]*data[4]  # 累计单种服装的销售金额
        return name, num, money ,sum_num ,sum_money                # 返回服装名称列表、销售数量列表、销售额列表、总销售量、总销售金额

    def yue_zhanbi(self):              # 每个月每个类型衣服的月销售额占比
        for month in range(0,12):
            name,num,money,sum_num,sum_moeny = shop.zhanbi(self,start=month ,stop=month+1 )    # 调用占比分析方法
            for i in range(len(name)):
                print("%s卖了%s元，销售额占%s月份总销售额的%s"% (name[i], round(money[i], 2), month+1, '{:.2%}'.format(money[i]/sum_moeny)))
            print("")
        return 0

    def max(self,quarter=5,moder="max"):        # 季度、年度最畅销服装分析
        if moder=="max":
            if quarter == 1:  # 第一季度 2、3、4
                name ,num ,money,sum,sum1 = shop.zhanbi(self,start=2-1,stop=4)

            elif quarter == 2:  # 第二季度 5、6、7
                name, num, money, sum, sum1 = shop.zhanbi(self, start=5-1, stop=7)

            elif quarter == 3:  # 第三季度 8、9、10
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
            for i in range(len(num)):    # 遍历的销售数量 《 下标为max的销售  max不变
                                         # 否则 max = i ,将下标i赋给max,定位销售数量最多的服装
                if num[max] >= num[i]:
                    max = max
                else:
                    max = i
            if quarter == 5:
                print("全年最畅销的衣服是%s,卖出了%s件" % (name[max], int(num[max])))
            else:
                print("第%s季度最畅销的衣服是%s,卖出了%s件" % (quarter, name[max], int(num[max])))

        elif moder=="min":                # 全年最不好卖的服装分析
            name, num, money, sum, sum1 = shop.zhanbi(self)
            min = 0
            for i in range(len(num)):       # 遍历的销售数量 > 下标为min的销售  min不变
                                            # 否则 min = i ,将下标i赋给min,定位销售数量最少的服装
                if num[min] < num[i]:
                    min = min
                else:
                    min = i
            print("全年销量最低的衣服是%s,卖出了%s件" % (name[min], int(num[min])))

        else:
            print("仅仅提供季度畅销查询和年销售最低查询。")
            return 0

    def show(self):                 # 打印功能选项
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
    choose = input("速度七十迈，心情自由自在，请选择：")
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
                for x in range(1,5):
                    a.max(quarter=x)
            elif y == "2":
                a.max()                 # 年度最畅销的服装
                a.max(moder="min")      # 年度最不好卖的服装
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
