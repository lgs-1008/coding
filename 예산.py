import random


d = [random.randint(1,5),random.randint(1,5),random.randint(1,5),random.randint(1,5)]
budget = random.randint(1,10)
print(d, budget)

d.sort()
answer = 0

for i in d:
    if budget>=i:
        budget = budget-i
        answer+=1

print(budget)
