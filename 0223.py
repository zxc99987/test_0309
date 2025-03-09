import random
'''
# 1. 基礎練習： Python判斷值是否為真
a = 10 > 5
b = 3 == 5
c = 'Python' != 'python' # !=: 不等於
d = len('apple') > 3 # len: 字串長度，1個字母長度為1

print(a, "\n", b, "\n", c, "\n", d) # \n: 程式讀到會自動換行
print("-" * 50)

# 1.1 進階練習： 自行輸入數字並Python判斷是否為真
money = input('請輸入消費金額：')
if int(money) > 100: # input輸入完，程式的資料型態是字串，加入int()將字串轉整數後才能判斷
    print("True")

else:
    print("請重新輸入。")

print("-" * 50)

# 2. 基礎練習： 自行輸入年齡，判斷是否成年
age = input('請輸入年齡：')
if int(age) > 18:
    print("成年。")

else:
    print("未成年。")

print("-" * 50)


# 2.2 進階練習： 建立一個菜單，使用input()讓使用者點餐，判斷是否在菜單中
menu = ['水餃', '蛋炒飯', '年肉麵', '湯包', '漢堡']
order = input('請輸入今天想要吃的餐點：')

if order in menu:
    print("已成功點餐。")

else:
    print("菜單上沒有這個品項，請重新輸入。")

print("-" * 50)


# 2.3 elif練習： 多個判斷條件使用elif
price = input('消費金額：')
if int(price) <= 500:
    price = int(price) * 0.9
    print("折扣後的金額：", price)

elif 500 < int(price) <= 1000: # int(price)>500 and int(price) <= 1000
    price = int(price) * 0.85
    print("折扣後的金額：", price)

elif 1000 <= int(price) < 1500:
    price = int(price) * 0.8
    print("折扣後的金額：", price)

else:
    price = int(price) * 0.7
    print("折扣後的金額：", price)

print("-" * 50)

# 2.4 基礎練習： input()輸入成績，考試分數分級
score = int(input("考試成績："))
if 90 <= score <= 100:
    print("A")

elif 80 <= score < 90:
    print("B")

elif 70 <= score < 80:
    print("C")

elif 60 <= score < 70:
    print("D")

else:
    print("Failed!")
print("-" * 50)

# 2.4.1 基礎練習： input()輸入成績，考試分數分級，超過100成績不合理
score = int(input("考試成績："))
if 90 <= score <= 100:
    print("A")

elif 80 <= score < 90:
    print("B")

elif 70 <= score < 80:
    print("C")

elif 60 <= score < 70:
    print("D")

elif score < 0 or score > 100:
    print("輸入成績不合理")

else:
    print("Failed!")

print("-" * 50)

# 2.4.2 進階練習：input()輸入餐點內容，判斷屬於哪一類食物
menu = {'滷肉飯': '飯類', '雞腿飯': '飯類', '炸雞': '炸類', '蛋包飯': '飯類', '雞米花': '炸類'}
order = input('今天想吃什麼？')
if order in menu: # if order == 滷肉飯 or order == 雞肉飯
    print(menu[order])

else:
    print("未知分類")

# 2.4.3 進階練習： input()年齡，判斷遊樂園入場門票
age = int(input("你的年紀？"))
if age < 13: # 先判斷是否為兒童
    if age < 6: # 是兒童，再判斷免費或半價入場
        print("票價：免費入場")
    else:
        print("票價：半價入場")

elif age <= 64:
    print("票價：原價入場")

else:
    print("票價：敬老票")

# 2.4.4 進階練習：input()消費金額，判斷是否符合優惠條件，再印出折扣金額
order_price = int(input('你的消費金額：'))
if order_price < 500:
    print("未達優惠門檻，消費滿500才享有折扣！")

elif 500 <= order_price < 699:
    order_price = order_price * 0.9
    print(f"消費金額打9折： {order_price:.1f}")

elif 700 <= order_price < 999:
    order_price = order_price * 0.85
    print(f"消費金額打85折： {order_price:.1f}")

elif order_price < 0:
    print("消費金額有誤。")

else:
    order_price = order_price * 0.8
    print(f"消費金額打8折： {order_price:.1f}")

# 2.4.5 進階練習： 猜密碼(使用巢狀迴圈)
a = random.randint(1, 99)
code = int(input('猜數字小遊戲！(請輸入1-99之間的數字)'))
while True:
    if code < a:
        code = int(input('數字太小，請再猜一次！'))
    elif code > a:
        code = int(input('數字太大，請再猜一次！'))
    else:
        print("答對了！")
        break


# 3. 基礎練習：for迴圈計數 
num = 0 # 從0開始
for i in range(1, 9): # 範圍設定1開始8結束
    num += i          # 第一次：0 = 0 + 1(1開始) = 1 此時num變為1 / 第二次：1 = 1 + 2(執行第2次) = 3 此時num變為3
    print(num)        # 從1開始8結束，每次執行相加結果都印出

# 3.1 基礎練習：建立菜單，使用for迴圈將菜單內的所有項目印出
menu = ['雞肉飯', '蛋炒飯', '牛肉麵', '水餃', '魷魚羹']
for i in menu:
    print(i)

print('*' * 50)
# 3.1.2 進階練習：建立價目表，使用for迴圈印出價目表內所有項目對應的價格
menu_price = {'雞肉飯': 30, '蛋炒飯': 50, '牛肉麵': 70, '水餃': 60, '魷魚羹': 55}
for i in menu_price:
    print("品項：", i, "價格：", menu_price[i])

print('*' * 50)

# 3.2 基礎練習：使用for迴圈列出1到10所有數字，用if判斷出偶數
for i in range(1, 11):      
    if i % 2 == 0:
        print(i, "是偶數")
    else:
        print(i, "是奇數")

print('*' * 50)
# 3.2.1 進階練習：清單numbers = [5, 12, 8, 3, 15, 7, 20]篩選出大於10的數字，再計算其總合
numbers = [5, 12, 8, 3, 15, 7, 20] # 建立名為numbers的清單
sum = 0 # 初始化名為sum的總和變數為0
for i in numbers: # i從清單內第一個數字開始執行，帶入下方i做判斷
    if i > 10:
        sum = sum + i # 總和 = 總和 + i，程式碼可以寫成 sum += i
        print(f'{i}大於10，總和為：{sum}')
    else:
        print(f'{i}小於10，不列入計算。')

print('*' * 50)


# 3.3 基礎練習： while迴圈，設定計數=0，每次加1，計數從1到100
count = 0
i = 1
while i < 101:
    count += i
    i += 1
print (count)
print("-" * 50)

# 3.3.1 進階練習：建立一個空的購物清單，讓使用者建立項目直到結束，印出購物清單
shopping_list = []

while True:
    wish_list = input('請輸入願望清單(輸入q結束許願)：')
    if wish_list.lower() == 'q':
        break
    shopping_list.append(wish_list)

print("許願列表：", shopping_list)
#print("願望清單共有" + str(len(shopping_list)) + "個物品等著被實現！ :)")
print("-" * 50)


# 3.4 基礎練習：要求使用者輸入一個1到100之間的數字，若輸入不符合範圍，則要求重新輸入，直到輸入正確為止
num = int(input('請輸入一個1到100之間的數字：'))
while num not in range(1, 101):
    print("輸入錯誤，請重新輸入數字。")
    num = int(input('請重新輸入：'))
    
print("-" * 50)

# 3.4.1 進階練習：登入系統，輸入正確密碼(python123)，輸入錯誤提示密碼錯誤請重試並要求重新輸入;連錯3次顯示多次輸入錯誤請稍後再試，結束程式並結束;輸入正確顯示登入成功
password = "python123"
num = input("請輸入密碼")
count = 1

if num != password:
    while True:
        if count < 3 :
            count += 1
            print("輸入錯誤，請重新再試")
            num = input("請輸入密碼")
        elif count >= 3 :
            print("錯誤太多次，請稍後再試")
            break
        else :
            print("登入成功")
else :
    print("登入成功")
'''

# 4.1 def基礎練習：建立函式(function)，輸入兩個數字來計算總合
def calculate(a, b):
    sum = a + b
    print(sum)
calculate(3, 5)
# 4.1.1 進階練習：建立函式，輸入一個字串並計算長度
def length(keyword):
    c = len(keyword)
    print(c)
length('James Bond')

# 4.1.2 建立函式： 輸出一個固定的數學計算結果(如：5+3)，返回結果
def cal():
    print("5+3=8")
cal()
# 4.1.3 進階練習：設定變數，數字=7，建立函式，計算數字的平方並顯示結果

# 專案練習：點餐機
# 第一步：歡迎詞
# 第二步：使用說明
# 第三步：讓使用者輸入餐點
# 第四步：判斷是否有在菜單內，有就繼續;沒有就提醒未在菜單內
# 第五步：使用者點餐完畢後，印出餐點內容與總價