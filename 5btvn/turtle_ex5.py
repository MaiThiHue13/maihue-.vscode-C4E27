from turtle import *
speed(0)
color("black")

def draw_star(x,y,length):
    for i in range(5):
        forward(length)
        right(144)

x=int(input("mời nhập x: "))
y=int(input("mời nhập y: "))
length=int(input("mời nhập chiều dài: "))
draw_star(x,y,length)
mainloop()
        
