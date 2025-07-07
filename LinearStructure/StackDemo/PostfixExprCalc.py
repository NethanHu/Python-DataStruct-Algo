from InfixExprConvert import infix2post
from LinearStructure.Stack import Stack

calc_enum = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}

infix_exp = '(17+8)/(4+6)*2-3'

print(infix2post(infix_exp))

def postfix_calculation(post_tokens: list[str]) -> float:
    op_stack = Stack()
    for token in post_tokens:
        if token.isdigit():
            op_stack.push(int(token))
        else:
            right_num = op_stack.pop()
            left_num = op_stack.pop()
            op_stack.push(calc_enum.get(token)(left_num, right_num))
    return op_stack.pop()

print(postfix_calculation(infix2post(infix_exp)))