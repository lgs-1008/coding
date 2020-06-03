s = "Zbcdefg"
def solution(s):
    s = list(s)
    stack = []
    for i in range(len(s)):
        stack.append(ord(s[i]))
    stack.sort(reverse=True)
    for i in range(len(stack)):
        stack[i] = chr(stack[i])
    return ''.join(stack)

print(solution(s))
