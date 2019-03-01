for i in range (20):
    print("*",end = '')
print
    


n=int(input("\nNhap so luong sao: "))
for i in range(n):
    print("*", end = '')
print()


n= int(input("\nNhap so luong n: "))
if n%2 == 0:
    for i in range(int(n/2)):
        print("x", end= '*')
else:
    for i in range (int((n-1)/2)):
        print("x", end='*')
print("x")
print()


n=int(input("Nhap n: "))
m=int(input("Nhap m: "))

for i in range(m):
    for j in range(n):
        print("*", end= '')
    print('')

    



















