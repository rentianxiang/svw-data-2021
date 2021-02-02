# Action1：求2+4+6+8+...+100的求和，用Python该如何写
result = 0
num = 2

while num <= 100:
    result = result + num
    num = num + 2

print(result)
