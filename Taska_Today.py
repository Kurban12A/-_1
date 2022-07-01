#
num = int(input())
for i in range(num+1):
    if i % 2 == 0:
        print(i)

#2
num = int(input())
for i in range(1, num // 2 + 1):
    if num % i == 0:
        print(i)




