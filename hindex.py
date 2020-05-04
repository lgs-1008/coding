citations = [3,0,6,1,5,7,8,24,13,65]
answer = 0
citations.sort()
for i in range(len(citations)):
    if citations[i] >= len(citations)-i:
        answer = len(citations)-i
        break

print(answer)
