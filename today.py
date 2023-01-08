


def is_prime(num):
    if num == 1:return 0
    for i in range(2, num):
        if num % i == 0:return 0
    return 1

a = int(input())
b = int(input())
for i in range(a, b+1):
    if is_prime(i) == 1:
        print(i)
