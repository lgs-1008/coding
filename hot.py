import heapq


answer = 0
scoville = [1,2,3,9,10,12]
K = 7
key = 0
heapq.heapify(scoville)
while len(scoville)>=1:
    check1 = heapq.heappop(scoville)
    if check1>K:
        #return -1
        key = 1
        break
    if len(scoville)>=1:
        check2 = heapq.heappop(scoville)
        scocheck = check1 + check2 * 2
        heapq.heappush(scoville, scocheck)
        answer += 1


if not key:
    answer = -1

print(answer)
