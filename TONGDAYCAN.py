import math

def tinh(n):
    total = 0
    for i in range(1, n+1):
        total += math.sqrt((i+1)/2*i)
    return total

n = int(input("N = "))
ans = "{:.7f}".format(tinh(n)) #Trong đó, ".7f" trong phương thức format() định dạng số thực với 7 chữ số sau dấu phẩy.
print("F(" + str(n) + ") = " + str(ans))