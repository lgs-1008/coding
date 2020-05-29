budgets = [120,110,140,150,203]
M = 785
def solution(budgets, M):
    check = 0
    mid = int((sum(budgets)//len(budgets)))+(int(M/len(budgets))/2
    budgets.sort()
    for i in range(len(budgets)):
        if budgets[i] <= mid:
            M-=budgets[i]
        else:
            check = i
            break

    sub = len(budgets)-(len(budgets)-check)
    answer = M//sub
    return answer






print(solution(budgets,M))
