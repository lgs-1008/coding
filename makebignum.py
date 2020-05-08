number = "44444444"
k = 4

def solution(number, k):
    stack = []
    for i,j in enumerate(number):
        while stack and stack[-1]<j and k>0:
            del stack[-1]
            k-=1
        if k==0:
            stack+=number[i:]
            break

        stack.append(j)

    if k>0:
        stack = stack[:-k]
    return "".join(stack)



print(solution(number,k))
