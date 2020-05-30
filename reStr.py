import re
def solution(s):
    answer = False
    if len(s)==4 or len(s)==6:
        if re.search('^\d+$',s):
            answer = True
    return answer


s = "3242"
print(re.search('^\d+$',s))
print(solution(s))
