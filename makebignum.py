number = "4177252841"
k = 4

def solution(number, k):
    check = list(number)
    j=0
    i=1
    while j!=k:
        if check[i-1]>check[i]:
            del check[i]
            j+=1
        elif check[i-1]<check[i]:
            del check[i-1]
            j+=1
        else:
            i+=2
    return "".join(check)



print(solution(number,k))
