a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
A = []
A.append(a)
A.append(b)
A.append(c)#add từng phần tử a,b,c vào mảng A
A.sort(reverse=False)#sau đó sắp xếp mảng A từ bé đến lớn
output = str(A[0])
for i in range(1,len(A)):
    if A[i]!=A[i-1]:
        output += " " + str(A[i])
print("Xep tang dan: " + output)
