skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA", "DAVES"]
alphaList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
skillList = list(skill)
answer = 0

for i in skillList:
    alphaList.remove(i)

for i in alphaList:
    for v in range(len(skill_trees)):
        skill_trees[v] = skill_trees[v].replace(i,"")

for i in range(len(skill_trees)):
    length = len(skill_trees[i])
    t = skill[0:length]
    if skill_trees[i]==t:
        answer+=1

print(answer)
