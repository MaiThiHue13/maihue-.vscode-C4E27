a= float(input("nhap can nang: "))
b= float(input("nhap chieu cao: "))

chisoBMI= a/(b*b*0.0001)
print(chisoBMI)

if chisoBMI <= 16:
    print (" ban bi thieu can tram trong")
elif 16 <= chisoBMI <= 18.5 :
    print("ban bi thieu can")
elif 18.5 <= chisoBMI <25:
    print("ban la nguoi binh thuong")
elif  25<= chisoBMI < 30:
    print("ban bi thua can")
else:
    print("ban bi beo phi")




