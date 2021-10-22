M = 13
table = [None]*M

def hashFn(key) :
    return key % M

def Ip_insert(key) : 
    id = hashFn(key)
    count = M
    while count > 0 and (table[id] != None and table[id] != -1) :
        id = (id + 1 + M) % M 
        count -= 1
    if count > 0 :
        table[id] = key
    return 

def Ip_search(key) :
    id = hashFn(key)
    count = M
    while count > 0 :
        if table[id] == None : 
            return None

        if table[id] != -1 and table[id] == key :
            return table[id]
        id = (id + 1 + M) % M
        count -= 1

    return None 

def Ip_delete(key) :
    id = hashFn(key)
    count = M
    while count > 0 :
        if table[id] == None : return
        if table[id] != -1 and table[id] == key :
            table[id] = -1
            return
        id = (id + 1 + M) % M
        count -= 1

print("최초 : ", table)
Ip_insert(45); print("45 삽입 : ", table)
Ip_insert(27); print("27 삽입 : ", table)
Ip_insert(88); print("88 삽입 : ", table)
Ip_insert(9); print("9 삽입 : ", table)
Ip_insert(71); print("71 삽입 : ", table)
Ip_insert(60); print("60 삽입 : ", table)
Ip_insert(46); print("46 삽입 : ", table)
Ip_insert(38); print("38 삽입 : ", table)
Ip_insert(24); print("24 삽입 : ", table)
Ip_delete(60); print("60 삭제 : ", table)
print("46 탐색 : ", Ip_search(46))
