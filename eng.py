n = 3
words =	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
answer = []
wordsCopy = []
wordsCopy.append(words[0])
checkWord = words[0]
for i in range(1, len(words)):
    if(checkWord[-1] != words[i][0]) or words[i] in wordsCopy:
        answer.append(i%n+1)
        answer.append(i//n+1)
        print(answer)
    wordsCopy.append(words[i])
    checkWord = words[i]
if answer is None:
    answer.append(0)
    answer.append(0)
    print(answer)
