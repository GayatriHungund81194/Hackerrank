num = 9
cnt = 0
if num is 1 or num is 0:
    print("neither prime not composite")
else:
    for i in range(1,num+1):
        if num%i is 0 :
            cnt = cnt + 1
if cnt > 2:
    print("Composite")
else:
    print("prime")