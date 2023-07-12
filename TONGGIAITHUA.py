def giaithua(n):
    gt = [1] * (n+1)
    for i in range(2,n+1):
        gt[i] = gt[i-1] * i
    return gt

def tinhtong(n):
    sum = 0
    gt = giaithua(n)
    for i in range(1,n+1):
        sum += gt[i]
    return sum

n = int(input("Nhap N duong: "))
print("F(" + str(n) + ") = " + str(tinhtong(n)))