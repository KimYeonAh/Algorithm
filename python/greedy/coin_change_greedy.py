def min_coin_greedy(coins, V) :
    count = []

    for i in coins :
        count.append(V//i)
        V %= i

    return count

coins = [500, 100, 50, 10, 5, 1]
V = 580
print("잔돈 액수 = ", V)
print("동전 종류 = ", coins)
print("동전 개수 = ", min_coin_greedy(coins, V))
