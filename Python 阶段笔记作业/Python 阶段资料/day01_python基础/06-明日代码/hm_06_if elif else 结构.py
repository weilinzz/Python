# 1. 定义 score 变量记录考试分数
score = float(input('请输入你的分数:'))
# 2. 如果分数是大于等于90分应该显示优
if score >= 90:
    print('优')
# 3. 如果分数是大于等于80分并且小于90分应该显示良
# elif (score >= 80) and score < 90:
elif score >= 80:  # 想要判断这个条件,一定意味着上一个条件不满足,
    print('良')
# 4. 如果分数是大于等于70分并且小于80分应该显示中
# elif (score >= 70) and score < 80:
elif score >= 70:
    print('中')
# 5. 如果分数是大于等于60分并且小于70分应该显示差
# elif (score >= 60) and score < 70:
elif score >= 60:
    print('差')
# 6. 其它分数显示不及格
else:
    print('不及格')


