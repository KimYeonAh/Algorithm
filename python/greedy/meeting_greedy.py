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
print(maxLen)
