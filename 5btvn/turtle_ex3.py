from turtle import *
speed(0)

def draw_square(length, colors):
    for i in range(4):
        color(colors)
        forward(length)
        left(90)
        

chieu_dai=int(input("Enter length: "))
mau_sac=str(input("Enter color: "))

draw_square(chieu_dai, mau_sac)


mainloop()

