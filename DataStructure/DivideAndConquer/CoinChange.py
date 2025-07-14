
coin_kinds = [25, 10, 5, 1]
rec_counts = 0

def rec_MC(rem_change: int, known_results: list[int]) -> int:
    global rec_counts
    rec_counts += 1
    best_coins_num = rem_change
    if rem_change in coin_kinds:
        known_results[rem_change] += 1
        return 1
    elif known_results[rem_change] > 0:
        return known_results[rem_change]
    else:
        for i in [c for c in coin_kinds if c <= rem_change]:
            num_coins = 1 + rec_MC(rem_change - i, known_results)
            if num_coins <= best_coins_num:
                best_coins_num = num_coins
                known_results[rem_change] = best_coins_num
    return best_coins_num


print(rec_MC(63, [0] * 64))
print(f"Totally recursive calling for {rec_counts} times")



