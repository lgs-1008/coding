import heapq


participant = ["mislav","stanko","mislav","ana"]
completion = ["stanko","ana","mislav"]
#for i in range(len(completion)):
#    participant.remove(completion[i])
#print("".join(participant))
heapq.heapify(participant)
heapq.heapify(completion)
while 1:
    if participant[0]==completion[0]:
        heapq.heappop(participant)
        heapq.heappop(completion)
    else:
        print(participant[0])
        break
