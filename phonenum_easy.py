def solution(phone_number):
    a = "*"*(len(phone_number)-4)
    b = a + phone_number[-4:]
    return b
