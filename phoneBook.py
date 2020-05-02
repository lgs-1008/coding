phone_book = ["119", "97684223", "1195524421"]
def solution(phone_book):
    for i in range(len(phone_book)):
        for v in range(len(phone_book)):
            if i==v:
                continue
            else:
                if phone_book[i]==phone_book[v][:len(phone_book[i])]:
                    return False
    return True
