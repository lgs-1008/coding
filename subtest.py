answers = [1,3,2,4,2]
k = len(answers)
first = ("12345"*2000)[:k]
second = ("21232425"*1250)[:k]
third = ("3311224455"*1000)[:k]
f = 0
s = 0
t = 0
for i in range(len(answer)):
    j = str(answer[i])
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
print(answer)
