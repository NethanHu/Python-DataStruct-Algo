from HashTable.ADTMap import HashTable

H = HashTable()
# put(key, data)
H.put(54, 'cat')
H.put(26, 'dog')
H.put(93, 'lion')
H.put(17, 'tiger')
H.put(77, 'bird')
H.put(31, 'cow')
H.put(44, 'goat') # hash(44) = 0. 与 hash(77) = 0 冲突
H.put(55, 'pig')  # hash(55) = 0. 再次冲突
H.put(20, 'chicken') # hash(20)=9, 与hash(93)=9 冲突

print("哈希表的 slots:", H.slots)
print("哈希表的 data:", H.data)
print("-" * 20)

# --- 开始查询 ---
# 1. 查询一个没有冲突的 key
print(f"查询 key=93: {H.get(93)}")

# 2. 查询一个经过1次 rehash 的 key (77的hash是0，54的hash是10，55的hash是0，44的hash是0)
# put(77,'bird') -> hash(77)=0. slots[0]='bird'
# put(44,'goat') -> hash(44)=0, 冲突, rehash(0)=1. slots[1]='goat'
# put(55,'pig') -> hash(55)=0, 冲突, rehash(0)=1, 冲突, rehash(1)=2. slots[2]='pig'
print(f"查询 key=44: {H.get(44)}")
print(f"查询 key=55: {H.get(55)}")

# 3. 查询一个不存在的 key
print(f"查询 key=100: {H.get(100)}")

# 4. 查询一个不存在但其哈希值会发生冲突的 key
# hash(22) = 0, 但 key=22 不在表中
print(f"查询 key=22: {H.get(22)}")