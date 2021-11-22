def startTime(rsv) :
    rsv.sort(key = lambda o: o[0])

    timeNum = 0
    meeting = []

    for i in rsv :
        if i[0] >= timeNum :
            timeNum = i[1]
            meeting.append((i[0], i[1]))
        
    return meeting

def endTime(rsv) :
    rsv.sort(key = lambda o: o[1], reverse = True)

    timeNum = 24
    meeting = []

    for i in rsv :
        if i[1] <= timeNum :
            timeNum = i[0]
            meeting.append((i[0], i[1]))
        
    return meeting

def meetingTime(rsv) :
    rsv.sort(key = lambda o: o[1]-o[0])

    meeting = []
 
    for i in rsv :
        flag = True
        if not meeting :
            meeting.append(i)
            continue
        
        for j in meeting :
            if j[0] <= i[0] and j[1] > i[0] :
                flag = False
                break
            if j[0] < i[1] and j[1] >= i[1] :               
                flag = False
                break
        
        if flag == True :
            meeting.append(i)
        else : 
            continue

    return meeting

reservation = [ (4, 6), (7, 14), (2, 5), (6, 7), (13, 20), (5, 9), (8, 13), (12, 18) ]

print(startTime(reservation))
print(endTime(reservation))
print(meetingTime(reservation))

start = startTime(reservation)
end = endTime(reservation)
meet = meetingTime(reservation)

maxLen = max(len(start), len(end), len(meet))

maxMeet = []

if len(start) == maxLen : maxMeet.append("시작시간 기준")
if len(end) == maxLen : maxMeet.append("종료시간 기준")
if len(meet) == maxLen : maxMeet.append("회의진행시간 기준")

print("가장 많은 회의를 진행할 수 있는 스케줄 : ", end='')

for i in range(len(maxMeet)) :
    if i != len(maxMeet)-1 :
        print(maxMeet[i], end=', ')
    else :
        print(maxMeet[i])
