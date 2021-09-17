

r1 = 6.44
r2 = 6.30

# n-time transfer
def compute(n):
    global r1
    need = 1687.5 * 12 * r1
    oneTime = need / n
    cost = 0
    num = 0
    while need > 0:
        num += 1
        # if num != 1:
        #     need *= 0.97 * (num)
        # amount = 0
        # if need >= oneTime:
        #     amount = oneTime
        # else:
        #     amount = need
        need -= oneTime
        cost += 150
        cost -= need * 0.03/12 * (12 / n)
    print(num)
    print(cost)


for i in range(1, 13):
    compute(i)

    