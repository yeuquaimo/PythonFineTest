s = input("Nhap S: ")
if not s.endswith("!!!"):
    while not s.endswith("!!!"):
        s += "!" 
print("Chuoi S sau khi xu ly: " + s)