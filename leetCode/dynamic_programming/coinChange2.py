## dfs 加 字典 深度优先遍历

def coinChange(coins, amount):
    from collections import defaultdict

    lookup = defaultdict(int)
    if amount < 1:
        return 0

# 定义新的函数helper

    def helper(amount):
        # print("amount:", amount)
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if lookup[amount]:
            print("haha")
            return lookup[amount]
        min_num = 2 ** 31 - 1

        # 用字典记录深度遍历过程中得到金额i的最小coins个数

        for coin in coins:            # 一直使用一种coins纵深遍历，
            print("coin is:",coin)
            print("amount:",amount)

            res = helper(amount - coin)    # 在这里迭代helper，直到res有返回值

            print("res:",res)
            # min_num = min(min_num,res + 1)
            if res >= 0 and res < min_num:
                min_num = res + 1

        lookup[amount] = min_num if min_num != 2 ** 31 - 1 else -1

        print("lookup:",lookup)  # 输出字典，字典包含 amount 个
        print(lookup[amount])
        return lookup[amount]

    print(helper(amount))
    return helper(amount)

if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11

    print(coinChange(coins, amount))




