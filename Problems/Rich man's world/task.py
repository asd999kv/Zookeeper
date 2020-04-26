deposit = int(input())
res = 0
while deposit <= 700000:
    deposit += deposit*0.071
    res += 1
print(res)