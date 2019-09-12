# bfs 广度优先遍历

def coinChange(coins, amount):
    res = 0
    cur = [0]
    visited = set()
    coins.sort()
    while cur:
        next_time = []
        res += 1
        for tmp in cur:
            for coin in coins:
                sum_num = tmp + coin
                if sum_num == amount:
                    return res
                elif sum_num > amount:
                    break
                elif sum_num < amount and sum_num not in visited:
                    next_time.append(sum_num)
                    visited.add(sum_num)
        cur = next_time
    return -1 if amount else 0

if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11

    print(coinChange(coins, amount))