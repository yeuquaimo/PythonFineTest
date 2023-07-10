import math
n = int(input("N = "))
total = 0
k = int(math.sqrt(n))
for i in range(1,k+1):
    if(n%i==0):
        total+=i
        total+=n//i
if k*k == n:
    total-=k
print("Tong cac uoc so cua " + str(n) + " la " + str(total))