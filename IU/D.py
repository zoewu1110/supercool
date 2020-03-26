flag=True
balance=0

drinks=[{"name":'可樂','price':20},
        {"name":'雪碧','price':35},
        {"name":'凱文','price':18000},
        {"name":'查理','price':56000},
        {"name":'珊朵拉','price':9865},
        {"name":'雷恩','price':564478},]

def depoist():
    global balance
    value = eval(input("儲存"))
    while value < 1:
        print("小氣鬼")
        value = eval(input("儲存"))
    balance += value
    print(f"total {balance}")

def buy():
    global balance,drinks
    print('\n要不要喝啦')
    for i in range(0, len(drinks)):
        print(f"({i + 1})\t{drinks[i]['name']} \t"
              f"{drinks[i]['price']}")
    choose = eval(input('choose:'))
    while choose < 1 or choose > 6:
        print("1-6")
        choose = eval(input('choose:'))
    buy = drinks[choose - 1]
    while balance <buy['price']:
        print('要加值嗎')
        want=input('yes or no')
        if want =='y':
            depoist()
        elif want=='n':
            break
        else:
            print("again")
    if balance < buy['price']:
        print('爛死了')
    else:
        print(f'已購買{buy["name"]} {buy["price"]}元')
        balance -= buy["price"]
        print(f'QQ${balance}元')

while flag:
    print("**********")
    select=eval(input('1.儲值\n2.購買\n3.查詢餘額\n4.離開\n選起來:'))
    if select ==1:
        # global balance
        # value = eval(input("儲存"))
        # while value < 1:
        #     print("小氣鬼")
        #     value = eval(input("儲存"))
        # balance += value
        # print(f"total {balance}")
        depoist()

    elif select==2:
        # print('\n要不要喝啦')
        # for i in range(0,len(drinks)):
        #     print(f"({i+1})\t{drinks[i]['name']} \t"
        #           f"{drinks[i]['price']}")
        # choose=eval(input('choose:'))
        # while choose <1 or choose>6:
        #     print("1-6")
        #     choose=eval(input('choose:'))
        # buy=drinks[choose-1]
        # if balance<buy['price']:
        #     print('爛死了')
        # else:
        #     print(f'已購買{buy["name"]} {buy["price"]}元')
        #     balance-=buy["price"]
        #     print(f'QQ${balance}元')
        buy()
    elif select==3:
        print(f'now total {balance}')

    elif select==4:
        print('chicken')
        flag=0
        break
    else:
        print('1-4 choose one')
        continue


