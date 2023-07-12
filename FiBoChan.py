def fibo(n):
    a,b = 0,1
    F = a+b
    while F < n:
        a=b
        b=F
        F=a+b
    return F
n = int(input("N = "))
result = fibo(n)
print("N la so fibonacci chan" if result%2==0 else
      "N khong phai la so fibonacci chan")

    