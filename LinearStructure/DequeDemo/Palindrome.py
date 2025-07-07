from LinearStructure.Deque import Deque


def judge_palindrome(word: str) -> bool:
    deque = Deque()
    for c in word:
        deque.add_rear(c)

    still_ok = True

    while deque.size() > 1 and still_ok:
        if deque.pop_front() != deque.pop_rear():
            still_ok = False

    return still_ok

print(judge_palindrome('abcdefg'))
print(judge_palindrome('radar'))