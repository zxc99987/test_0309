'''
# Python基礎課程 - 數學運算練習
a = 5
b = 2
print ("加法：", a + b)
print("減法：", a - b)
print("乘法：", a * b)
print("整數除法：", a // b)
print("餘數：", a % b)
print(type(a)) # type查找資料型態：int(正整數) str(字串)...
print("-" * 50) # 與下一個練習題做區隔的符號


# Python基礎課程 - 字串串接練習
storeName = 'Stark Industrial'
message = 'Welcome to ' + storeName + '!\n' + 'This is Ironman home.'
print(storeName + "!\n" + message)
print("-" * 50) # 與下一個練習題做區隔的符號


# Python基礎課程 - 取出字串中第幾個字母
voc = storeName[3] # voc變數是volcabulary縮寫，變數名稱可以自己取
print(voc)
print("-" * 50) # 與下一個練習題做區隔的符號


# Python基礎課程 - list(清單)練習 使用中括弧[]編輯清單內容，程式從0開始
# 以水果舉例
food_list = ['Apple', 'Banana', 'Guava']
print(food_list)
food_list.append('Strawberry') # append語法，加在清單的最右邊
print(food_list)
print(food_list[1:2]) # 索引清單第2個的資料 使用[數字:數字](數字自行更換，從第幾個開始索引到第幾個結束，最後一個數字不會索引出來)
print("-" * 50)


# Python基礎課程 - list(清單)進階練習，Dictionary(字典)用法，使用大括弧{}編輯字典內容
# 以水果舉例，新增價格
food_menu = {'Apple': 25, 'Banana': 20, 'Guava': 35, 'Strawberry': 40}
print("水果價目表：", food_menu)
# 使用[]索引字典內，某個水果的價格 中括弧內是水果名
print("草莓的價格：", food_menu["Strawberry"])
# 修改價格
food_menu['Guava'] = 15
print("修改後芭樂的價格為：", food_menu["Guava"])
print("-" * 50)


# Python基礎課程 - input()，自行輸入要印出的資料
meal = input('請輸入餐點內容：')
print(meal)
print("-" * 50)


# Python基礎課程 - input()進階練習
# 用input做一個自我介紹名片，設定3個變數：姓名、年齡、職業
# 第一步：印出你好，我是___，我今年__歲，職業是__
# 第二步：印出5年後我是__歲
name = input('請輸入姓名：')
age = input('請輸入年齡：')
occ = input('請輸入職業：')
print("你好，我是" + name + "，我今年" + age + "歲，職業是" + occ)
print("5年後我是" + str(int(age) + 5) + "歲")
print("-" * 50)


# Python基礎課程 - input()進階練習，建立dictionary名片
# 第一步：使用input，以添加值的方式新增名片資料
# 第二步：印出名片資料
nameTag = {}
nameTag['name'] = input('請輸入姓名：')
nameTag['age'] = input('請輸入年齡：')
print("名片資料：", nameTag)


# Python基礎課程 - 建立空的願望清單
# 讓使用者自行輸入許願列表
# 印出願望清單
# 印出願望清單有多少東西要實現
shopping_list = []

while True:
    wish_list = input('請輸入願望清單(輸入q結束許願)：')
    if wish_list.lower() == 'q':
        break
    shopping_list.append(wish_list)

print("許願列表：", shopping_list)
print("願望清單共有" + str(len(shopping_list)) + "個物品等著被實現！ :)")
print("-" * 50)
'''

#  Python基礎課程 - 建立空的購物清單
# 第一步：先設定好一個價目表(蘋果、草莓、鳳梨)
# 第二步：建立一個空的購物清單
# 第三步：讓使用者輸入想購買的水果(蘋果、草莓、鳳梨其中之一)
# 第四步：印出購物清單
# 第五步：定義價格變數來計算購物清單的總價
# 第六步：印出 "你顯買的水果有：__，總共價格為：__元"
# 第七步：水果攤有周年慶打9折，印出購物清單以及原價還有折扣後的價格
fruit_list = {'蘋果': 30, '草莓': 35, '鳳梨': 50}
buy_list = []
buy_list = input('請輸入想購買的水果：')
print("你想要買的水果是：", buy_list)
total_price = fruit_list[buy_list]
print("你購買的水果是：" + buy_list + "，總共的價格為：" + str(total_price) + "元！")
print("今天水果攤周年慶打9折，你購買的水果是：" + buy_list + "，打折前的價格為：" + str(total_price) + "元！"
      + "折扣後的價格為：" + str(total_price * 0.9) + "元！")