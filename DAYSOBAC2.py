def tinh(n):
    total = 0
    for i in range(1,n+1):
        total += n / ( (i+1)/2*i + i/3*(i-1)*(i+1) )
    return total

n = int(input("N = "))
ans = "{:.7f}".format(tinh(n))
print("F(" + str(n) + ") = " + str(ans))