import random
# 不能一样
JN1 = 4
JN2 = 5
JN3 = 8
JN4 = 9
JN5 = 13
GU = 4

sum_spend_list = []

for i in range(1000):
    spend = 0
    count = 0
    ALL_JN = set()
    while True:
        ran_num = random.random()
        if len(ALL_JN) == 0:
                ALL_JN.add(JN1)
                count += 1
                spend += JN1

        elif len(ALL_JN) == 1:
            SPARE_JN = {JN1,JN2}
            GET_JN = SPARE_JN - ALL_JN    # 将要打的技能
            if ran_num <= 0.8:
                ALL_JN.add(list(GET_JN)[0])
                count += 1
            else:
                ALL_JN.pop()
                ALL_JN.add(list(GET_JN)[0])
                count += 1
            spend += list(GET_JN)[0]

        elif len(ALL_JN) == 2:
            SPARE_JN = {JN1,JN2,JN3}
            GET_JN = SPARE_JN - ALL_JN    # 将要打的技能
            if ran_num <= 0.6:
                ALL_JN.add(list(GET_JN)[0])
                count += 1
            else:
                ALL_JN.pop()   # 顶掉的技能
                ALL_JN.add(list(GET_JN)[0])  
                count += 1
            spend += list(GET_JN)[0]

        elif len(ALL_JN) == 3:
            SPARE_JN = {JN1,JN2,JN3,JN4}
            GET_JN = SPARE_JN - ALL_JN    # 将要打的技能
            if ran_num <= 0.4:
                ALL_JN.add(list(GET_JN)[0])
                count += 1
            else:
                ALL_JN.pop()   # 顶掉的技能
                ALL_JN.add(list(GET_JN)[0])  
                count += 1
            spend += list(GET_JN)[0]
        # 直接五技能，没有内丹
        elif len(ALL_JN) == 4:
            SPARE_JN = {JN1,JN2,JN3,JN4,JN5}
            GET_JN = SPARE_JN - ALL_JN    # 将要打的技能
            # if JN5 not in GET_JN:     # 如果打的技能不是JN5，则出发固神丹保护
            #     if ran_num <= 0.2:
            #         ALL_JN.add(list(GET_JN)[0])
            #         count += 1
            #     else:
            #         ALL_JN.pop()   # 顶掉的技能
            #         while True:
            #             if JN5 not in ALL_JN: # 固神保护
            #                 # print("触发固神保护")
            #                 ALL_JN.add(JN5)  
            #                 ALL_JN.pop()
            #             else:
            #                 break
            #         ALL_JN.add(list(GET_JN)[0])  
            #         count += 1
            #     spend += GU
            # else:
            if ran_num <= 0.2:
                ALL_JN.add(list(GET_JN)[0])
                count += 1
            else:
                ALL_JN.pop()   # 顶掉的技能
                ALL_JN.add(list(GET_JN)[0])  
                count += 1
            spend += list(GET_JN)[0]
        
        elif len(ALL_JN) == 5:
            print(spend)
            sum_spend_list.append(spend)
            break
        # print(f"目前状态：{ALL_JN}，第{count}打书，花费了{spend}")
    print(f"五技能模板：第{i}轮，平均花费{sum(sum_spend_list)/len(sum_spend_list)}")


    # while True:
    #     ran_num = random.random()
    #     if len(ALL_JN) == 0:
    #             ALL_JN.add(JN1)
    #             count += 1
    #             spend += JN1

    #     elif len(ALL_JN) == 1:
    #         SPARE_JN = {JN1,JN2}
    #         GET_JN = SPARE_JN - ALL_JN    # 将要打的技能
    #         if ran_num <= 0.75:
    #             ALL_JN.add(list(GET_JN)[0])
    #             count += 1
    #         else:
    #             ALL_JN.pop()
    #             ALL_JN.add(list(GET_JN)[0])
    #             count += 1
    #         spend += list(GET_JN)[0]

    #     elif len(ALL_JN) == 2:
    #         SPARE_JN = {JN1,JN2,JN3}
    #         GET_JN = SPARE_JN - ALL_JN    # 将要打的技能
    #         if ran_num <= 0.5:
    #             ALL_JN.add(list(GET_JN)[0])
    #             count += 1
    #         else:
    #             ALL_JN.pop()   # 顶掉的技能
    #             ALL_JN.add(list(GET_JN)[0])  
    #             count += 1
    #         spend += list(GET_JN)[0]

    #     elif len(ALL_JN) == 3:
    #         SPARE_JN = {JN1,JN2,JN3,JN4}
    #         GET_JN = SPARE_JN - ALL_JN    # 将要打的技能
    #         if ran_num <= 0.25:
    #             ALL_JN.add(list(GET_JN)[0])
    #             count += 1
    #         else:
    #             ALL_JN.pop()   # 顶掉的技能
    #             ALL_JN.add(list(GET_JN)[0])  
    #             count += 1
    #         spend += list(GET_JN)[0]
    #     # 先是四技能，然后再五技能
    #     elif len(ALL_JN) == 4:
    #         SPARE_JN = {JN1,JN2,JN3,JN4,JN5}
    #         GET_JN = SPARE_JN - ALL_JN    # 将要打的技能
    #         if ran_num <= 0.2:
    #             ALL_JN.add(list(GET_JN)[0])
    #             count += 1
    #         else:
    #             ALL_JN.pop()   # 顶掉的技能
    #             ALL_JN.add(list(GET_JN)[0])  
    #             count += 1
    #         spend += list(GET_JN)[0]
        
    #     elif len(ALL_JN) == 5:
    #         print(spend)
    #         sum_spend_list.append(spend)
    #         break
    #     # print(f"目前状态：{ALL_JN}，第{count}打书，花费了{spend}")
    # print(f"内丹五技能模板：第{i}轮，平均花费{sum(sum_spend_list)/len(sum_spend_list)}")

