import random
# 技能价格不能一样
JN1 = 2
JN2 = 4
JN3 = 6
JN4 = 8

sum_spend = 0
state = 0
count = 0

ALL_JN = set()

while state < 5:
    ran_num = random.random()
    if len(ALL_JN) == 0:
        sum_spend += JN1
        ALL_JN.add(JN1)
    elif len(ALL_JN) == 1: # 4选3
        if ran_num <= 0.75: # 成功75%
            if JN2 not in ALL_JN:
                ALL_JN.add(JN2)
                sum_spend += JN2
            else:
                ALL_JN.add(JN1)
                sum_spend += JN1
        else:   # 失败25%
            ALL_JN.pop()
            if JN2 not in ALL_JN:
                ALL_JN.add(JN2)
                sum_spend += JN2
            else:
                ALL_JN.add(JN1)
                sum_spend += JN1
    elif len(ALL_JN) == 2: # 4选2
        print(sum_spend)
        break
