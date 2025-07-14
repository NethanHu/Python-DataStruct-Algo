from LinearStructure.Stack import Stack

dec_num = 2333

def base_converter(input_dec: int, base: int) -> list[str]:
    stack = Stack()

    while input_dec != 0:
        stack.push(input_dec % base)
        input_dec = input_dec // base

    target_num = []
    for n in stack:
        target_num.append(str(n))

    return target_num


def dec2bin(input_dec: int) -> str:
    return ''.join(base_converter(input_dec, 2))

def dec2oct(input_dec: int) -> str:
    return ''.join(base_converter(input_dec, 8))

def dec2hex(input_dec: int) -> str:
    mapping = {
        '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'
    }
    target = base_converter(input_dec, 16)
    for i in range(len(target)):
        if len(target[i]) > 1:
            target[i] = mapping.get(target[i])
    return ''.join(target)


print('Hex(10) value:', dec_num)
print('Bin(2) value:', dec2bin(dec_num))
print('Oct(8) value:', dec2oct(dec_num))
print('Hex(16) value:', dec2hex(dec_num))
