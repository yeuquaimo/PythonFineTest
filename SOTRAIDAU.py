a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
print("Khong co cap so trai dau" if a >= 0 and b>=0 and c>=0 or a<=0 and b<=0 and c<=0 else
      "Co cap so trai dau")