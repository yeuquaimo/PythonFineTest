def tinh(n):
    total = 1
    for i in range(2,n+1):
        total += ( (i+1)/2*i )**(1/i)
    return total
n = int(input("N = "))
ans = "{:.7f}".format(tinh(n))
print("F(" + str(n) + ") = " + str(ans) )