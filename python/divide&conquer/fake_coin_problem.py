import numpy as np
import random

coin = np.ones(10000) 
index = random.randrange(0, 10000) #가짜 동전의 위치
coin[index] = 0
count = 0

def fake_coin(list, count) :
    if coin[count] == 0 :
        return count
    
    pos1 = len(list)//3
    pos2 = pos1*2

    group1 = int(sum(list[0:pos1]))
    group2 = int(sum(list[pos1:pos2]))

    if group1 < group2 :
        return fake_coin(list[0:pos1], count)
    elif group1 > group2 :
        count += group1
        return fake_coin(list[pos1:pos2], count)
    else :
        count += (group1 + group2)
        return fake_coin(list[pos2:len(list)], count)

print("가짜 동전 index : ", index)
print("가짜 동전 찾았다! : ", fake_coin(coin, count))
