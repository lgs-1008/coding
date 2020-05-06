participant = ["mislav","stanko","mislav","ana"]
completion = ["stanko","ana","mislav"]

def solution(participant, completion):
    hash = {}
    for i in participant:
        hash[i] = hash.get(i, 0) + 1
    for i in completion:
        hash[i] -= 1

    answer = "".join([i for i, j in hash.items() if j==1])
    return answer

print(solution(participant, completion))
