print("NHAP BANG GIA:")
gia_tri = {}
xet = {}
while 1:
    name = input("  Ten mat hang: ")
    if name == '':
        break
    gia_ban = float(input("  Gia ban hang: "))
    gia_tri[name] = gia_ban
    xet[name] = False

print("NHAP HANG TON:")

while True:
    name = input("  Ten mat hang: ")
    if name == '':
        break
    hang_ton = int(input("  So luong ton kho: "))
    for ten, gia in gia_tri.items():
        if name == ten:
            xet[ten] = True
            gia_tri[ten] = gia*hang_ton

for ten,gia in gia_tri.items():
    if xet[ten] == False:
        gia_tri[ten] = 0.00

print("THONG KE HANG TON:")
sorted_gia_tri = sorted(gia_tri.items(), key=lambda x:(-x[1], x[0]), reverse=False)

#tìm ra tên mặt hàng có độ dài lớn nhất
ten_dai_nhat = max(len(ten) for ten in gia_tri)

for ten, gia in sorted_gia_tri:
    print("  {:<{}} {:>6.2f}".format(ten, ten_dai_nhat , gia))
 
#code chạy                                                 #expected
#NHAP BANG GIA:                                            #NHAP BANG GIA:
#  Ten mat hang: tao                                       #  Ten mat hang: tao
#  Gia ban hang: 3                                         #  Gia ban hang: 3
#  Ten mat hang: chuoi                                     #  Ten mat hang: chuoi
#  Gia ban hang: 3                                         #  Gia ban hang: 3
#  Ten mat hang: cam                                       #  Ten mat hang: cam
#  Gia ban hang: 4                                         #  Gia ban hang: 4
#  Ten mat hang:                                           #  Ten mat hang:
#NHAP HANG TON:                                            #NHAP HANG TON:
#  Ten mat hang: tao                                       #  Ten mat hang: tao
#  So luong ton kho: 3                                     #  So luong ton kho: 3
#  Ten mat hang: chuoi                                     #  Ten mat hang: chuoi
#  So luong ton kho: 3                                     #  So luong ton kho: 3
#  Ten mat hang:                                           #  Ten mat hang:
#THONG KE HANG TON:                                        #THONG KE HANG TON:
#  chuoi    9.00                                           #  chuoi    9.00
#  tao      9.00                                           #  tao      9.00
#  cam      0.00                                           #  cam      0.00