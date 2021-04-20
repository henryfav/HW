import turtle
import random

WIDTH = 1024
HEIGHT = 768


def mondrian(x, y, w, h, t):
    '''draw rectangles and fill them with color randomly, and then react
to what's already drawn so the rectangles ultimately fit well in our
1024x768 frame
'''
    random_width = random.uniform(120, w * 1.5)
    random_height = random.uniform(120, h * 1.5)
    split = random.uniform(1/3, 2/3)#split point used
    points = [[x, y], [x, y + h], [x + w, y + h], [x + w, y]]
    drawRectangle(points, t)
#if and all elif's have dimensional conditions that if true they will run
    if w > (WIDTH / 2) and h > (HEIGHT / 2):
        '''here it creates a first random rectangle, and then a second reactive
to the first, and a third reactive to the two before
'''
        width_one = w * split
        height_one = h * split
        mondrian(x, y, width_one, height_one, t)#create first rectangle
        box2 = y + height_one
        height2 = h - height_one
        mondrian(x, box2, width_one, height2, t)#create second rectangle
        #create third rectangle
        mondrian(x + width_one, box2, w - width_one, height2, t)
        mondrian(x + width_one, y, w - width_one, height_one, t)

    elif w > (WIDTH/2):
        width_one = w * split
        mondrian(x, y, width_one, h, t)
        mondrian(x + width_one, y, w - width_one, h, t)
    elif h > (HEIGHT / 2):
        height_one = h * split
        mondrian(x, y, w, height_one, t)
        mondrian(x, y + height_one, w, h - height_one, t)
    elif random_height < h and random_width < w:
        width_one = w * split
        height_one = h * split
        mondrian(x, y, width_one, height_one, t)
        box2 = y + height_one
        height2 = h - height_one
        mondrian(x, box2, width_one, height2, t)
        
        mondrian(x + width_one, box2, w - width_one, height2, t)
        mondrian(x + width_one, y, w - width_one, height_one, t)
    elif random_height < h:
        height_one = h * split
        mondrian(x, y, w, height_one, t)
        mondrian(x, y + height_one, w, h - height_one, t)
    elif random_width < w:
        width_one = w * split
        mondrian(x, y, width_one, h, t)
        mondrian(x + width_one, y, w - width_one, h, t)

    else:
        fillcolor(points, t)
        
def fillcolor(points,myTurtle):
    '''fills rectangle with a random color
'''
    r = random.random()
    if r < 0.0833:
        myTurtle.fillcolor("red")
    elif r < 0.1667:
        myTurtle.fillcolor("blue")
    elif r < 0.25:
        myTurtle.fillcolor("yellow")
    else:
        myTurtle.fillcolor("white")

    myTurtle.begin_fill()    
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[3][0],points[3][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()
    
def drawRectangle(points,myTurtle):
    '''draws rectangles based on what has already been drawn and where
'''
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[3][0],points[3][1])
    myTurtle.goto(points[0][0],points[0][1])
    

#creates turtle, its attributes and its coordinate environment
def main():
    wn = turtle.Screen()
    wn.setworldcoordinates(0, 0, WIDTH + 1, HEIGHT + 1)
    turt = turtle.Turtle()
    turt.speed(0)
    turt.pensize(3)
    mondrian(0, 0, WIDTH, HEIGHT, turt)

if __name__ == '__main__':
    main()
