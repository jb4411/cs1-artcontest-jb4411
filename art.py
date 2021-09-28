"""
file: art.py
description: Draws a large gradient to use as the background of the picture, it
then draws 12 overlapping nine-sided polygons to create an intricate nine sided
figure. A black box is then drawn to act as the "floor" and a mountain range is
drawn to make the skyline. Lit candles are then recursively drawn on the "floor"
from the bottom of the screen to the skyline. Finally, the turtle is hidden and
a message telling the user that the turtle has completed the drawing is printed.
Then a file called "Jesse Burdick-Pless's Art Show Submission.eps" is created in
the home directory of this python file and the program is paused.
language: python3
author: jb4411@g.rit.edu Jesse Burdick-Pless
"""
import turtle
import math

def gradient_while(radius=100,r="default",g="default",b="default",red=0,green=0,blue=0,step=1,depth=1,):
    """
    This function takes up to nine parameters, and based on the parameters draws
    a circular gradient with an outer radius based on the parameter when the
    function is called. The gradient is drawn by drawing circles with decreasing
    radii and incrementally changing the color of the turtle based on the
    parameters when the function is called for each additional circle.
    :precondition: The pen is down.
    :precondition: The turtle is facing 90 degrees to the right of where the
    gradient should be drawn.
    :postcondition: The turtle’s location is the same as when this function
    started.
    :postcondition: The pen is down.
    :postcondition: The turtle is facing east.
    :postcondition: Color filling has ended.
    """
    final_depth = (radius/step)
    color_step = (1/final_depth)
    while radius > 0:
        turtle.color(red,green,blue)
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()

        #increment red
        if r != "default":
            if r == "+":
                red += color_step
            elif r == "-":
                red -= color_step
            elif r == "--":
                if red > 0:
                    old = red
                    red -= color_step
                    if red < 0:
                        red = old
        else:
            red = red

        #increment green
        if g != "default":
            if g == "+":
                green += color_step
            elif g == "-":
                green -= color_step
            elif g == "++":
                green += color_step/3
            elif g == "--":
                green -= color_step/3
        else:
            green = green

        #increment blue
        if b != "default":
            if b == "+":
                blue += color_step
            elif b == "-":
                blue -= color_step   
        else:
            blue = blue
        radius -= step

def draw_candle(length):
    """
    This function draws a singular lit candle with a glow behind it whose length
    is based on the parameter when the function is called.
    :precondition: The turtle is facing east.
    :precondition: The turtle is at the middle bottom of where the candle should
    be drawn.
    :postcondition: The turtle’s location is the same as when this function
    started.
    :postcondition: The pen is up.
    :postcondition: The turtle is facing east.
    :postcondition: Color filling has ended.
    """
    turtle.up()
    turtle.right(90)
    turtle.forward(length/(1500/67))
    turtle.left(90)
    turtle.down()
    gradient_while(length/2,"+","++","default",0,0,0)
    turtle.up()
    turtle.left(90)
    turtle.forward(length/(1500/67))
    turtle.right(90)
    turtle.setheading(0)

    turtle.up()
    turtle.back(length/6)
    turtle.down()
    turtle.pencolor("#ffffff")
    turtle.fillcolor("#ffffd4")
    turtle.begin_fill()

    #draw candlestick
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.up()
    turtle.forward(length/3)
    turtle.right(90)
    turtle.down()
    turtle.forward(length)
    turtle.right(90)
    turtle.up()
    turtle.forward(length/3)
    turtle.end_fill()

    turtle.fillcolor("#fadeaa")
    
    #fill rectangle at top
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.begin_fill()
    turtle.forward(length/3)
    turtle.right(90)
    turtle.down()
    turtle.forward(length/(500/6.67))
    turtle.up()
    turtle.right(90)
    turtle.forward(length/3)
    turtle.right(90)
    turtle.down()
    turtle.forward(length/(500/6.67))
    turtle.up()
    turtle.end_fill()

    #setup to draw top circles
    turtle.right(90)
    turtle.forward(length/6)
    turtle.right(90)
    turtle.forward(length/(500/29))
    turtle.left(90)

    #setup and draw first arc
    turtle.down()
    turtle.up()
    turtle.circle(length/3,330)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(length/3,60)
    turtle.end_fill()
    turtle.up()
    turtle.circle(length/3,330)
    
    #setup and draw second arc
    turtle.left(90)
    turtle.forward((length/(1500/67))+(length/(500/29)))
    turtle.down()
    turtle.left(90)
    turtle.up()
    turtle.circle(length/3,330)
    turtle.begin_fill()
    turtle.down()
    turtle.circle(length/3,60)
    turtle.end_fill()
    turtle.up()
    turtle.circle(length/3,330)
    turtle.up()
    turtle.left(90)
    turtle.forward(length/(1500/67))
    turtle.left(90)

    #setup to draw third arc
    turtle.forward(length/6)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length/6)
    turtle.left(90)
    turtle.forward(length/(1500/67))
    turtle.left(90)
    
    #draw third arc
    turtle.up()
    turtle.circle(length/3,330)
    turtle.down()
    turtle.fillcolor("#ffffd4")
    turtle.begin_fill()
    turtle.circle(length/3,60)
    turtle.end_fill()
    
    #setup to draw flame
    turtle.up()
    turtle.circle(length/3,330)
    turtle.left(90)
    turtle.forward(length/(1500/67))
    turtle.forward(length)
    turtle.forward(length/14)

    #draw flame
    turtle.right(90)
    gradient_while(length/4.8,"+","++","default",0,0,0)

    #draw wick
    turtle.pensize(length/(250/3))
    turtle.color(0,0,0)
    turtle.right(90)
    turtle.forward(length/14)
    turtle.left(180)
    turtle.down()
    red = .045
    green = 0
    blue = 0
    distance = 0
    turtle.color(red,green,blue)
    while distance < length/8:
        turtle.forward(length/800)
        red += 1/125
        green += 1/375
        blue = 0
        turtle.color(red,green,blue)
        distance += length/800

    #return to starting position
    turtle.up()
    turtle.back(distance)
    turtle.pensize(1)
    turtle.right(180)
    turtle.forward(length)
    turtle.left(90)
    

def draw_candle_rec(length,depth=5):
    """
    This function recursively draws lit candles whose lengths are based on the
    parameter when the function is called with each additional row of candles
    having half the length of the previous row.
    :precondition: The turtle is facing east.
    :precondition: The turtle is at the middle bottom of where the first candle
    should be drawn.
    :postcondition: The turtle’s location is the same as when this function
    started.
    :postcondition: The pen is up.
    :postcondition: The turtle is facing east.
    :postcondition: Color filling has ended.
    """
    if depth == 1:
        #draw candle
        draw_candle(length)
    else:
        #draw candle
        draw_candle(length)
        
        #prepare to draw next candle
        turtle.forward((4*length)/5)
        turtle.left(90)
        turtle.forward((4*length)/5)
        turtle.right(90)
        
        #make recursive call
        draw_candle_rec(length/2,depth-1)
        
        #prepare to draw next candle
        turtle.left(90)
        turtle.back((4*length)/5)
        turtle.right(90)
        turtle.back((4*length)/5)
        turtle.back((4*length)/5)
        turtle.left(90)
        turtle.forward((4*length)/5)
        turtle.right(90)
        
        #make recursive call
        draw_candle_rec(length/2,depth-1)
        
        #prepare to draw next candle
        turtle.right(90)
        turtle.forward((4*length)/5)
        turtle.left(90)
        turtle.forward((4*length)/5)
        
def draw_star(length,depth=9):
    """
    This function recursively draws a nine pointed star where the length of each
    line in the star is based on the parameter when the function is called.
    :precondition: The pen is down.
    :precondition: The turtle is at the middle bottom of where the nine pointed
    star should be drawn.
    :postcondition: The turtle’s location is the same as when this function
    started.
    :postcondition: The pen is down.
    :postcondition: The turtle is facing the same direction it was when this
    function was called.
    """
    turtle.down()
    if depth > 0:
        turtle.forward(length)
        turtle.left(160)
        draw_star(length,depth-1)

def draw_triangle_star(length,depth=9):
    """
    This function recursively draws a nine pointed star where the length of
    each line in the polygon is based on the parameter when the function is
    called.
    :precondition: The pen is down.
    :precondition: The turtle is at the middle bottom of where the nine pointed
    star should be drawn.
    :postcondition: The turtle’s location is the same as when this function
    started.
    :postcondition: The pen is down.
    :postcondition: The turtle is facing the same direction it was when this
    function was called.
    """
    turtle.down()
    if depth > 0:
        turtle.forward(length)
        turtle.left(80)
        draw_triangle_star(length,depth-1)

def draw_triple_triangles(length,depth=3):
    """
    This function recursively draws a triangle where the length of each line in
    the triangle is based on the parameter when the function is called.
    :precondition: The pen is down.
    :postcondition: The turtle’s location is the same as when this function
    started.
    :postcondition: The pen is down.
    :postcondition: The turtle is facing the same direction it was when this
    function was called.
    """
    turtle.down()
    if depth > 0:
        turtle.forward(length)
        turtle.left(120)
        draw_triple_triangles(length,depth-1)

def draw_all_triangles(x,y,color,pensize):
    """
    This function calls draw_triple_triangles three times from a different
    position each time to draw a nine sided figure made out of three overlapping
    triangles. The bottom center point of the figure, the turtle's color and the
    pensize are all based on the parameters when the function is called.
    :postcondition: The pen is up.
    :postcondition: The turtle is facing east.
    :postcondition: The turtle’s location is the same as when this function
    started.
    """
    turtle.up()
    turtle.goto(x,y)
    turtle.color(color)    

    turtle.pensize(pensize)
    turtle.up()
    turtle.left(90)
    turtle.forward(47)
    turtle.right(30)
    draw_triple_triangles(181.8)

    turtle.up()
    turtle.goto(97.91+x,y+35.63)#-314.37)

    turtle.setheading(0)
    turtle.left(130)
    turtle.forward(47)
    turtle.right(30)
    draw_triple_triangles(181.8)

    turtle.up()
    turtle.goto(-97.91+x,y+35.63)#-314.37)
    turtle.setheading(0)
    turtle.left(50)
    turtle.forward(47)
    turtle.right(30)
    draw_triple_triangles(181.8)
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(0)
    
def draw_figures(x,y):
    """
    This function repeatedly calls draw_all_triangles, draw_triangle_star and
    draw_star to draw 12 overlapping nine-pointed stars to create an intricate
    nine sided figure.
    :postcondition: The pen is up.
    :postcondition: The turtle is facing 80 degrees to the left of the angle it
    was facing when the function was called.
    """
    draw_all_triangles(x,y,"#04113d",4)
    turtle.up()
    turtle.setheading(0)
    draw_all_triangles(x,y,"#ffffff",.5)

    turtle.color("#04113d") 
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.pensize(6)
    turtle.speed(7)
    turtle.left(40)
    draw_triangle_star(195.5)

    turtle.color("#ffffff")
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.pensize(1)
    turtle.speed(7)
    turtle.left(40)
    draw_triangle_star(195.7)

    turtle.color("#04113d")
    turtle.pensize(6)
    turtle.up()
    turtle.setheading(0)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.left(40)
    draw_triangle_star(175.5)

    turtle.color("#ffffff")
    turtle.up()
    turtle.setheading(0)
    turtle.pensize(1) 
    turtle.speed(7)
    turtle.left(40)
    draw_triangle_star(175.7)

    turtle.setheading(0)
    turtle.up()
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
       

    turtle.color("#04113d")
    turtle.speed(0)
    turtle.left(80)
    turtle.pensize(5)
    draw_star(300)
    
    turtle.color("#ffffff")
    turtle.pensize(1)
    draw_star(300)
    
def mountain_range():
    """
    This function draws a mountain range to act as the skyline for the final
    picture.
    :precondition: The pen is down.
    :precondition: The turtle is at the bottom left of where the mountains
    should be drawn.
    :postcondition: The pen is down.
    :postcondition: The turtle is 185.9 pixels east of where it was when the
    function started.
    :postcondition: The turtle is 14.79 pixels north of where it was when the
    function started.
    :postcondition: The turtle is facing 56 degrees to the right of the angle it
    was facing when the function was called.
    """
    turtle.left(70)
    turtle.forward(27)
    turtle.right(137)
    turtle.forward(7)
    turtle.left(128)
    turtle.forward(20)
    turtle.right(137)
    turtle.forward(30)
    turtle.up()
    turtle.back(15)
    
    
    turtle.left(111)
    turtle.forward(1)
    turtle.down()
    turtle.forward(19)
    turtle.right(117)
    turtle.forward(8)
    turtle.left(132)
    turtle.forward(16)
    turtle.right(127)
    turtle.forward(13)
    turtle.left(132)
    turtle.forward(5)
    turtle.right(125)
    turtle.forward(18)
    turtle.up()
    turtle.back(4)
    
    
    turtle.left(130)
    turtle.forward(1)
    turtle.down()
    turtle.forward(17)
    turtle.right(130)
    turtle.forward(6)
    turtle.left(112)
    turtle.forward(13)
    turtle.right(113)
    turtle.forward(6)
    turtle.left(138)
    turtle.forward(3)
    turtle.right(113)
    turtle.forward(20)
    turtle.up()
    turtle.back(5)
    
    
    turtle.left(124)
    turtle.forward(1)
    turtle.down()
    turtle.forward(17)
    turtle.right(130)
    turtle.forward(6)
    turtle.left(118)
    turtle.forward(14)
    turtle.right(111)
    turtle.forward(13)
    turtle.left(130)
    turtle.forward(5)
    turtle.right(124)
    turtle.forward(31)
    turtle.up()
    turtle.back(7)
    
    turtle.left(124)
    turtle.forward(1)
    turtle.down()
    turtle.forward(25)
    turtle.right(130)
    turtle.forward(6)
    turtle.left(118)
    turtle.forward(20)
    turtle.right(137)
    turtle.forward(33)
    turtle.left(135)
    turtle.forward(4)
    turtle.right(127)
    turtle.forward(33)
     
def main():
    """
    This function begins by drawing a large gradient to use as the background of
    the picture, it then draws 12 overlapping nine-pointed stars to create an
    intricate nine sided figure. A black box is then drawn to act as the "floor"
    and a mountain range is drawn to make the skyline. Lit candles are then
    recursively drawn on the "floor" from the bottom of the screen to the
    skyline. Finally, the turtle is hidden and a message telling the user that
    the turtle has completed the drawing is printed. Then a file called "Jesse
    Burdick-Pless's Art Show Submission.eps" is created in the home directory of
    this python file and the program is paused.
    :postcondition: The turtle is facing east.
    :postcondition: The turtle is 481.22 pixels east of where it was when the
    function started.
    :postcondition: The turtle is 130 pixels north of where it was when the
    function started.
    :postcondition: The pen is down.
    :postcondition: The turtle is hidden.
    :postcondition: The program is paused.
    """
    turtle.setup(width=950,height=787) 
    turtle.title("Jesse Burdick-Pless's Art Show Submission.")
    turtle.tracer(0,0)
    turtle.up()
    turtle.goto(0,-200)
    turtle.down()
    gradient_while(600,"default","default","+",0,0,0)
    draw_figures(0,50)

    turtle.up()
    turtle.goto(-600,130)
    turtle.setheading(0)
    turtle.down()
    turtle.color("black")
    turtle.begin_fill()
    sides = 0
    while sides < 4:
        sides += 1
        turtle.forward(1200)
        turtle.right(90)
    turtle.end_fill()
    turtle.up()
    
    turtle.up()
    turtle.goto(0,-350)
    turtle.setheading(0)
    draw_candle_rec(300)
   
    turtle.pencolor("#0d34b5")
    turtle.fillcolor("black")
    turtle.up()
    turtle.goto(-606,130)
    turtle.down()

    count = 0
    while count < 6:
        count += 1
        turtle.begin_fill()
        mountain_range()
        turtle.setheading(0)
        turtle.up()
        turtle.goto(turtle.xcor()-4.7,130)
        turtle.end_fill()
        turtle.down()

    turtle.update() 
    turtle.hideturtle()
    print("The turtle has finished drawing the picture!")
    turtle.getscreen().getcanvas().postscript(file="Jesse Burdick-Pless's Art Show Submission.eps", colormode='color')
    turtle.done()

main()



