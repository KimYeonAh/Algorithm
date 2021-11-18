def knapSack_fractional_greedy(obj, W) :
    obj.sort(key = lambda o: o[2]/o[1], reverse=True) #단위무게당 가치로 sort

    totalValue = 0

    for i in obj :
        if W - i[1] >= 0 :
            W -= i[1]
            totalValue += i[2]
        else :
            totalValue += (i[2]/i[1])*W

    return totalValue

obj = [ ("A", 10, 80), ("B", 12, 120), ("C", 8, 40) ]
print("W = 28 ", obj)
print("부분적인 배낭(28): ", knapSack_fractional_greedy(obj, 28), end = '\n\n')

obj = [ ("A", 10, 60), ("B", 40, 40), ("C", 20, 100), ("D", 30, 120) ]
print("W = 50 ", obj)
print("부분적인 배낭(50): ", knapSack_fractional_greedy(obj, 50))
