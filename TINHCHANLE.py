a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
print("Cung tinh chan le" if a%2==0 and b%2==0 and c%2==0 or a%2==1 and b%2==1 and c%2==1 else
      "Khac tinh chan le")