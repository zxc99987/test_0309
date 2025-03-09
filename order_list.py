# 建立一個購物清單，礦泉水/蘋果/衛生紙
# 第一步：刪除衛生紙 第二步：新增雞肉 第三步：呼叫購物清單 第四步：找出購物清單中第二個品項

order_list = ['礦泉水', '蘋果', '衛生紙']
order_list.remove('衛生紙')
order_list.append('雞肉')
print(order_list)
print(order_list[1])
print("-" * 50)

# 建立一個成績單
# 學生有：小明、小華、小王
# 成績分別為：70、60、80
# 第一步：印出成績表 第二步：校長想知道小華的成績 第三步：新增一個轉學生小美，成績是90

score_list = {'小明': 70, '小華': 60, '小王': 80}
print("成績單：", score_list)
print("小華的成績：", score_list['小華'])
score_list['小美'] = 90
print("新增小美的成績：", score_list)
print("成績單共有" + str(len(score_list)) + "位學生") # len()->查找清單、字典內有幾個元素，或查找字串有幾個字元
print("-" * 50)