import math

def coin_change_min_count(coins: list[int], amount: int) -> (int, list[int]):
    dp_table = [math.inf] * (amount + 1)
    dp_last_coin = [0] * (amount + 1) # 加入我们要记录的硬币组合表，我们只存这个change选了什么面值的即可
    dp_table[0] = 0
    for change in range(1, amount + 1):
        local_min_coin_counts = dp_table[change]
        for k in [k for k in coins if k <= change]:
            rem = change - k
            if dp_table[rem] < local_min_coin_counts:
                local_min_coin_counts = dp_table[int(rem)] + 1
                dp_last_coin[change] = k # 如果选择c面值找到了最优解，就在这个位置保存选了什么面值的硬币
            dp_table[change] = local_min_coin_counts

    cur_amount = amount
    coin_comb = []
    while cur_amount > 0:
        last_used_coin = dp_last_coin[cur_amount]
        coin_comb.append(last_used_coin)
        cur_amount -= last_used_coin

    return int(dp_table[amount]), coin_comb

change = 128
coin_kinds = [1, 5, 10, 21, 25]

print(coin_change_min_count(coin_kinds, change))
