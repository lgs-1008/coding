array = [1,5,2,6,3,7,4]
commands = [[2,5,3], [4,4,1], [1,7,3]]
answer = []
for v in range(len(commands)):
    i = commands[v][0]
    j = commands[v][1]
    k = commands[v][2]
    num = array[i-1:j]
    num.sort()
    answer.append(num[k-1])

print(answer)
