n = int(input("Nhap N: "))
A = []
B = []
for i in range(1,n+1):
    value = input("Nhap gia tri thu " + str(i) + ": ")
    if '.' in value:
        try:
            A.append(float(value))
        except:
            B.append(value)
    else:
        try:
            A.append(int(value))
        except:
            B.append(value)
if A != []:
    tbc = sum(A) / len(A)
    print("TBC cua A =",tbc)
print("B =",B)                    
