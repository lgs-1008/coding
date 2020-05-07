w = 2
h = 3

def gong(w,h):
    if w<h:
        (w,h) = (h,w)
    while h!=0:
        (w,h) = (h, w%h)
    return w

def solution(w,h):
    g = gong(w,h)
    answer = (w*h)-(w+h-g)
    return answer

print(solution(w,h))
