def startTime(rsv) :
    rsv.sort(key = lambda o: o[0])

    timeNum = 0
    meeting = []

    for i in rsv :
        if i[0] >= timeNum :
            timeNum = i[1]
            meeting.append((i[0], i[1]))
        
    return meeting

reservation = [ (4, 6), (7, 14), (2, 5), (6, 7), (13, 20), (5, 9), (8, 13), (12, 18) ]

print(startTime(reservation))
