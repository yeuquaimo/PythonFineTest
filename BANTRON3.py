#n = int(input("So nguoi ngoi quanh ban: "))
#a = list(range(1, n+1))
#i = 0
#while len(a) > 1:
#    i += 2
#    i %= len(a)
#    del a[i]

#print("Nguoi o lai cuoi cung la nguoi thu", a[0])


#n = int(input("So nguoi ngoi quanh ban: "))
#a = list(range(1, n+1))

#k = 0
#while len(a) > 1:
#    k = (k + 3 - 1) % len(a)
#    del a[k]

#print("Nguoi o lai cuoi cung la nguoi thu", a[0])

n = int(input("So nguoi ngoi quanh ban: "))

def find_last_person(n):
    last_person = 0
    for i in range(2, n+1):
        last_person = (last_person + 3) % i
    return last_person

last_person = find_last_person(n)
print("Nguoi o lai cuoi cung la nguoi thu", last_person+1)