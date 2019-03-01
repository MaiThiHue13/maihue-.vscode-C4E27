1, The Boolean data type can be one of two values, either True/ False
    EX1:
    a=[1,2,3,4,5]
    "1" in a
    True
    "6" in a
    False

    EX2:
    x = 5
    y = 8

    print("x == y:", x == y)
    print("x != y:", x != y)
    print("x < y:", x < y)
    print("x > y:", x > y)
    print("x <= y:", x <= y)
    print("x >= y:", x >= y)
    Output
    x == y: False
    x != y: True
    x < y: True
    x > y: False
    x <= y: True
    x >= y: False

    EX3:
    Hue = "Hue"
    hue = "hue"

    print("Hue == hue: ", Hue == hue)
    Output
    Hue == hue:  False



3, The outer conditional contains two branches. The second branch (the else from the outer) contains another if statement, which has two branches of its own.
 Those two branches could contain conditional statements as well.
if  X <  y : 
    print ( "x nhỏ hơn y" ) 
other : 
    if  x  >  y : 
        print ( "x lớn hơn y" ) 
    other : 
        print ( "x và y phải bằng nhau" )