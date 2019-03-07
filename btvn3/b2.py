list = [5,7,300,90,24,50,75]
list_max = []

print("hello, my name is Hue , these are my ship sizes: ")
print(list)
max1 = max(list)
list_max.append(max1)
print("Now my biggest ship has size ",max1," let shear it !")
index = list.index(max1)
list[index] = 8
print("After shearing here is my flock: ")
print(list)


n = int(input("Input number of Month: "))
for i in range (n):
    for j in range (7):
         list[j] += 50 
    print("Month ",i+1)
    print("One month has passed, now here is my flock:")
    print(list)
    max_for = max(list)
    list_max.append(max_for)
    index_max = list.index(max_for)
    print("Now my biggest ship has the sizes ",max(list)," let's shear it !")
    list[index_max] = 8
    print("After shearing here is my flock:")
    print(list)

Total = sum(list_max)
Price = Total * 2
print("My flock has size in total",Total)
print(Total,"* 2$ =",Price," $")