s = input("Nhap chuoi: ")
if not s.endswith("!!!"):
    while not s.endswith("!!!"):
        s+= '!'
print("Chuoi sau khi bo sung dau cham than: '"+ s +"'")