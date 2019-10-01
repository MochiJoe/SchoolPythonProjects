#Good Luck Greeting Card
#Nolaundron 'Ray' Harris

from graphics import*
import random



def main():

    

    #create graphics window
    win=GraphWin("Good Luck Card",500,801)
    win.setCoords(-252,-398,248,402)
    win.setBackground("Black")

    #create random color list
    #Random color list
 
    colorList=["Yellow", "Green", "Pink", "Red", "Blue", "Purple", "Orange"]
    colorList2=["Green","Red", "Purple", "Orange"]
    colorList3=["Yellow", "Pink", "Black", "Blue"]
    boarderColor=random.choice(colorList)

    #Ask user to input a name into an entry box
    Entrytxt="Who would you like to send a 'Good Luck' card to:"      
    nameEntrytxt=Text(Point(0,250),Entrytxt)
    nameEntrytxt.setSize(18)
    nameEntrytxt.setTextColor(boarderColor)
    nameEntrytxt.setStyle("bold")
    nameEntrytxt.draw(win)
        
    #nameEntrytxt=Text(Point(0,250),"Who would you like to send a 'Start Game' card to:")
    #nameEntrytxt.setSize(18)
    #nameEntrytxt.setTextColor("Yellow")
    #nameEntrytxt.draw(win)

    #Input text box for user
    nameEntry=Entry(Point(0,200),30)
    nameEntry.setFill("Pink")
    nameEntry.setSize(18)
    nameEntry.setTextColor("Lime Green")
    nameEntry.draw(win)

    

    

#Card Boarders
##########
#####
#
    win.getMouse()
    win.close()


    win=GraphWin("Greeting Card",500,801)
    win.setCoords(-252,-398,248,402)
    win.setBackground("Light Blue")        
    #Left card boarder
    for i in range(-400,426,25):
        lBoarderColor=random.choice(colorList)
        lBoarder=Rectangle(Point(-252,400-i+i),Point(-200,i+i))
        lBoarder.setFill(lBoarderColor)
        lBoarder.draw(win)

        lBoarder2=Circle(Point(-177,0+i),10)
        lBoarder2.setFill(lBoarderColor)
        lBoarder2.draw(win)
        

    #Right card boarder
    for j in range(-400,426,25):
        rBoarderColor=random.choice(colorList)
        rBoarder=Rectangle(Point(200,400-j+j),Point(250,j+j))
        rBoarder.setFill(rBoarderColor)
        rBoarder.draw(win)

        rBoarder2=Circle(Point(175,0+j),10)
        rBoarder2.setFill(rBoarderColor)
        rBoarder2.draw(win)

    #Top card boarder
    for k in range(-250,500,50):
        tBoarderColor=random.choice(colorList)
        tBoarder=Rectangle(Point(-200+k,400),Point(k+k,350))
        tBoarder.setFill(tBoarderColor)
        tBoarder.draw(win)

    #Bottom card boarder
    for l in range(-250,500,50):
        bBoarderColor=random.choice(colorList)
        bBoarder=Rectangle(Point(-200+l,-400),Point(l+l,-350))
        bBoarder.setFill(bBoarderColor)
        bBoarder.draw(win)

    #Confetti
    for m in range(10):
        confettiColor=random.choice(colorList2)
        x=random.randint(-200,200)
        y=random.randint(-350,350)
        confetti=Polygon(Point(x,y),Point(-x,y),Point(x,-y),Point(-x,-y))
        confetti.setFill(confettiColor)
        confetti.draw(win)
        
#Start Game Card
    randomColor2=random.choice(colorList2)
    randomColor3=random.choice(colorList3)
    inputName=nameEntry.getText()
    Name=str(inputName)
    
    areyouText=Text(Point(0,300),"Good Luck")
    areyouText.setTextColor(randomColor3)
    areyouText.setStyle("bold")
    areyouText.setSize(30)
    areyouText.draw(win)

    ontestText=Text(Point(0,0),"On Your Finals")
    ontestText.setTextColor(randomColor3)
    ontestText.setStyle("bold")
    ontestText.setSize(30)
    ontestText.draw(win)

    cardName=Text(Point(0,-300),Name+"!!!!!!")
    cardName.setTextColor(randomColor3)
    cardName.setSize(30)
    cardName.setStyle("bold")
    cardName.draw(win)
    
        
        


    
main()
