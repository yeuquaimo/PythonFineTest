n = int(input("So nguoi ngoi quanh ban: "))
#a = [0] *(n)
#for i in range(0,n):
#    a[i] = i+1
a = list(range(1, n+1))
i=0
while 1:
    if len(a) == 1:
         break
    i+=2
    if len(a) > 2:
        if i == len(a):
            i = 0
        if i > len(a):
            i = i - len(a)
        del a[i]
    else:                #Khi mang con hai phan tu thi thuc hien ham else nay
        if i - 2 == 1:
            del a[1]
        else:
            del a[0]
print("Nguoi o lai cuoi cung la nguoi thu",a[0])




