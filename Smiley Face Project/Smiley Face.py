from graphics import*

def main():
    win=GraphWin('Face',500,500)
    win.setBackground("Black")
    win.setCoords(0,0,500,500)


    head = Circle(Point(250,250),200)
    head.setFill("Yellow")
    head.draw(win)

    leye= Oval(Point(100,290),Point(200,320))
    leye.setFill("Black")
    leye.draw(win)
    leye.setWidth(20)

    reye=Line(Point(300,310), Point(400,310))
    reye.draw(win)
    reye.setFill("Black")
    reye.setWidth(5)

    mouth=Polygon(Point(125,200),Point(375,200),Point(300,100),Point(200,100))
    mouth.draw(win)
    mouth.setFill("Black")
    

    ltooth=Rectangle(Point(200,200),Point(230,180))
    ltooth.setFill("White")
    ltooth.setOutline("White")
    ltooth.draw(win)

    rtooth=Rectangle(Point(270,200),Point(300,180))
    rtooth.setFill("White")
    rtooth.setOutline("White")
    rtooth.draw(win)

    tongue=Oval(Point(215,125),Point(285,75))
    tongue.draw(win)
    tongue.setFill("Red")

    tonguepart=Line(Point(250,125),Point(250,100))
    tonguepart.setWidth(3)
    tonguepart.draw(win)

    halftongue=Rectangle(Point(215,99),Point(285,75))
    halftongue.setFill("Yellow")
    halftongue.setOutline("Yellow")
    halftongue.draw(win)

main()
