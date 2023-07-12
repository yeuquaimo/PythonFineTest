def tinh(n):
    return sum(int(digit) for digit in str(n))

n = int(input("N = "))
N = 2**n
print("Tong = " + str(tinh(N)))