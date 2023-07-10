def main():
    N = int(input("Nhap N: "))
    A = []
    B = []
    C = []

    for i in range(1,N+1):
        value = input("Nhap gia tri thu "+ str(i) + ": ")
        if '.' in value:
            try:
                B.append(float(value))
            except ValueError:
                C.append(value)
        else:
            try:
                A.append(int(value))
            except ValueError:
                C.append(value)

    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    print("A =", A)
    print("B =", B)
    print("C =", C)

main()
#Trong vòng lặp for, chúng ta kiểm tra kiểu dữ liệu của giá trị nhập vào bằng cách kiểm tra xem có dấu chấm (.) hay không.
#Nếu có dấu chấm, chúng ta cố gắng chuyển giá trị thành số thực bằng hàm float(), nếu không thành công, giá trị đó không phải là kiểu thực và tất nhiên cx k phải kiểu nguyên và được thêm vào danh sách C.
#Nếu không có dấu chấm, chúng ta cố gắng chuyển giá trị thành số nguyên bằng hàm int(), nếu không thành công, giá trị đó không phải là kiểu nguyên và tất nhiên cx k phải kiểu thực và được thêm vào danh sách C.
#Cuối cùng, chúng ta sắp xếp ba danh sách A, B và C theo thứ tự giảm dần bằng cách sử dụng phương thức sort(reverse=True) và in ra màn hình.