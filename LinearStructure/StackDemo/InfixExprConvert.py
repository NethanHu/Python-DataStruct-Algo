import re

from LinearStructure.Stack import Stack

priority = {
    '+': 1, '-': 1, '*': 2, '/': 2, '@': 3
}

def split_op_num(expr: str) -> list[str]:
    return re.findall(r'\d+|[+\-*/@()]', expr)

def infix2post(expr: str) -> list[str]:
    tokens = split_op_num(expr)
    post_list = []
    op_stack = Stack()

    for token in tokens:
        if 'a' <= token.lower() <= 'z' or '0' <= token <= '9':  # 单纯的字母或者数字
            post_list.append(token)

        elif token == '(':
            op_stack.push(token)

        elif token == ')':
            # 如果是右括号，将栈中直到左括号的运算符全部弹出
            top_token = op_stack.pop()
            while top_token != '(':
                post_list.append(top_token)
                top_token = op_stack.pop()

        else:
            # 如果是其它的运算符
            while not op_stack.is_empty() and \
                   op_stack.peek() != '(' and \
                   priority.get(token) <= priority.get(op_stack.peek()):
                post_list.append(op_stack.pop())
            op_stack.push(token)


    while not op_stack.is_empty():
        post_list.append(op_stack.pop())

    return post_list

# infix_exp = '((a+b)-c*d@e)/f'
# print(''.join(infix2post(infix_exp)))