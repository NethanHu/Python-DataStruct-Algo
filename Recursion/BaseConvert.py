HEX_MAPPING = {
    '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'
}

def recur_base_convert(num_left: int, base: int, rem_list: list[str]) -> list[str]:
    if num_left < base:
        rem_list.append(str(num_left))
        return rem_list
    rem_list.append(str(num_left % base))
    num_left = num_left // base
    return recur_base_convert(num_left, base, rem_list)

def base_convert(dec_num: int, base: int) -> list[str]:
    rem_list = recur_base_convert(dec_num, base, [])
    rem_list.reverse()
    return rem_list

def dec2bin(dec_num: int) -> str:
    return ''.join(base_convert(dec_num, 2))

def dec2oct(dec_num: int) -> str:
    return ''.join(base_convert(dec_num, 8))

def dec2hex(dec_num: int) -> str:
    hex_num = base_convert(dec_num, 16)
    hex_chars = [HEX_MAPPING.get(rem, rem) for rem in hex_num]
    return ''.join(hex_chars)

dec_num = 23333
print('Hex(10) value:', dec_num)
print('Bin(2) value:', dec2bin(dec_num))
print('Oct(8) value:', dec2oct(dec_num))
print('Hex(16) value:', dec2hex(dec_num))