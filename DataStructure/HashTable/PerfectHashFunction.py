import hashlib

text_1 = bytearray('Hello, world!', 'utf-8')
text_2 = bytearray('hello world', 'utf-8')

print(hashlib.md5(text_1).hexdigest())
print(hashlib.md5(text_2).hexdigest())

def simple_hash(astring: str, table_size: int):
    sum = 0
    for pos in range(len(astring)):
        sum += ord(astring[pos])
    return sum % table_size