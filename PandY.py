a = "awfea"
def solution(s):
    up = s.upper()
    p = up.count("P")
    y = up.count("Y")
    if p == y:
        return True
    else:
        return False

print(solution(a))
