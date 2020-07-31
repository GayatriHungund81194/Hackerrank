number = input()
num1 = raw_input().split(" ")
number2 = input()
num2 = raw_input().split(" ")
cnt = 0
for i in range(len(num1)):
    if num1[i] in num2:
        cnt = cnt + 1
print(cnt)