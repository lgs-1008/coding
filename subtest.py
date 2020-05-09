answers = [1,3,2,4,2]

def solution(answers):
    first = ("12345"*2000)[:len(answers)]
    second = ("21232425"*1250)[:len(answers)]
    third = ("3311224455"*1000)[:len(answers)]
    f = 0
    s = 0
    t = 0
    for i in range(len(answers)):
        j = str(answers[i])
        if j == first[i]:
            f+=1
        if j == second[i]:
            s+=1
        if j == third[i]:
            t+=1


    answer = []
    if (f>s and f>t) or (f==s and f>t) or (f>s and f==t):
        answer.append(1)
    elif (s>f and s>t) or (s==f and s>t) or (s>f and s==t):
        answer.append(2)
    elif (t>s and t>f) or (t==s and t>f) or (t>s and t==f):
        answer.append(3)
    elif f==s==t:
        answer.append(1)
        answer.append(2)
        answer.append(3)

    return answer

print(solution(answers))
