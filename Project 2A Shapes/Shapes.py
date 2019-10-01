from graphics import*

def main():
    win=GraphWin('Shapes',600,400)
    win.setBackground("Black")
    win.setCoords(0,0,600,400)

    triangle=Polygon(Point(50,250),Point(150,350),Point(250,250))
    triangle.setFill("Turquoise")
    triangle.setOutline("White")
    triangle.setWidth(5)
    triangle.draw(win)

    rectangle=Rectangle(Point(350,350),Point(550,250))
    rectangle.setFill("Orange")
    rectangle.setOutline("White")
    rectangle.setWidth(5)
    rectangle.draw(win)

    circle=Circle(Point(100,100),50)
    circle.setFill("Green")
    circle.setOutline("White")
    circle.setWidth(5)
    circle.draw(win)

    square=Rectangle(Point(250,150),Point(350,50))
    square.setFill("Blue")
    square.setOutline("White")
    square.setWidth(5)
    square.draw(win)

    pentagon=Polygon(Point(475,50),Point(450,100),Point(500,150),Point(550,100),Point(525,50))
    pentagon.setFill("Purple")
    pentagon.setOutline("White")
    pentagon.setWidth(5)
    pentagon.draw(win)

    

main()
