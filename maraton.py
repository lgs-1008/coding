participant = ["mislav","stanko","mislav","ana"]
completion = ["stanko","ana","mislav"]
#for i in range(len(completion)):
#    participant.remove(completion[i])
#print("".join(participant))
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i,v in zip(participant,completion):
        if i!=v:
            return(i)
    return participant[-1]

print(solution(participant,completion))
