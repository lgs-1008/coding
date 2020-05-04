numbers = [3, 30, 34, 5, 9]

numbers = list(map(str, numbers))
numbers.sort(key = lambda i: (i*4)[:4], reverse=True)
answer = "".join(numbers)
answer = str(int(answer))
print(answer)
