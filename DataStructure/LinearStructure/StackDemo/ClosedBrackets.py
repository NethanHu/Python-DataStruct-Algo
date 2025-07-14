from LinearStructure.Stack import Stack

verse = {
    ')': '(', ']': '[', '}': '{'
}

str_input = '{{([][])}()}{}([])'

def judge_fined_brackets(brackets: str) -> bool:
    stack = Stack()
    bracket_list = list(brackets)

    if not bracket_list:
        print("Empty brackets!")
        return False

    for s in bracket_list:
        if s == '(' or s == '[' or s == '{':
            stack.push(s)
        else:
            if stack.is_empty():  # s is not None but stack is empty
                return False

            elif stack.peek() == verse.get(s):
                stack.pop()

            else:
                return False

    return True if stack.is_empty() else False

print(judge_fined_brackets(str_input))