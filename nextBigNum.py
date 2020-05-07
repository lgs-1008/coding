n = 15

def solution(n):
    a = bin(n)
    a = a.replace("0","")
    a = a.replace("b","")
    b = n+1
    while b:
        t = bin(b)
        t = t.replace("0","")
        t = t.replace("b","")
        if a==t:
            return b
        b+=1


print(solution(n))
