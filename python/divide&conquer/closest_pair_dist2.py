import math

minNum = 0
pointList = [""]*2

def distance(p1 ,p2):
    tmp = math.sqrt((p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)
    
    global minNum

    if minNum == 0 or minNum > tmp:
        minNum = tmp
        pointList[0] = p1[0]
        pointList[1] = p2[0]
        
    return tmp

def closest_pair(p):
    n = len(p)
    mindist = float("inf")
    for i in range(n-1):
        for j in range(i+1,n):
            dist = distance(p[i], p[j]) 
            if dist < mindist:
                mindist= dist
    return mindist

def strip_closet(P,d):
    n = len(P)
    d_min = d
    P.sort(key = lambda point: point[1]) 
   
    for i in range(n) :
        j = i + 1
        while j < n and (P[j][2] - P[i][2]) < d_min :
            dij = distance(P[i],P[j])
            if dij < d_min :
               d_min = dij
               
            j += 1
    return d_min

def closest_pair_dist(P,n): 
    if n <= 3:
        return closest_pair(P)
   
    mid = n //2
    mid_x = P[mid][1]
   
    dl = closest_pair_dist(P[:mid], mid)
    dr = closest_pair_dist(P[mid:], n-mid)
    d= min(dl,dr)
   
    Pm = []
    for i in range(n):
        if abs(P[i][1] - mid_x) < d: 
            Pm.append(P[i])
           
    ds = strip_closet(Pm, d)
    return min(d, ds)
    

p = [("A", 2, 3), ("B", 12, 30), ("C", 40, 50), ("D", 5, 1), ("E", 12, 10),("F", 3, 4)]
p.sort(key = lambda k : k[0])

print("가장 가까운 두 점의 거리", closest_pair_dist(p, len(p)))
print("가까운 점은 ",pointList[0], "와 ", pointList[1], "입니다.")
