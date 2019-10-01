#Miles to Kilometers
#Nolaundron 'Ray' Harris





from graphics import*

def main():
#Set up Miles entry window and get number input
#
#
    win=GraphWin("Miles to Kilometers",600,400)
    win.setBackground("Red")
    win.setCoords(0,0,60,40)

    nextStepBox=Rectangle(Point(20,15),Point(40,5))
    nextStepBox.setWidth(5)
    nextStepBox.setOutline("Yellow")
    nextStepBox.setFill("Navy Blue")
    nextStepBox.draw(win)
    nextSteptxt1=Text(Point(30,12.5),"Click For")
    nextSteptxt1.setTextColor("Yellow")
    nextSteptxt1.setSize(30)
    nextSteptxt1.setStyle("bold")
    nextSteptxt1.draw(win)
    nextSteptxt2=Text(Point(30,7.5),"Next Window")
    nextSteptxt2.setTextColor("Yellow")
    nextSteptxt2.setSize(30)
    nextSteptxt2.setStyle("bold")
    nextSteptxt2.draw(win)
    #Get input in miles
    textInputpromp=Text(Point(30,36.75),"Enter how many miles you'd "
                   "like to convert to Kilometers:")
    textInputpromp.setTextColor("Yellow")
    textInputpromp.setSize(20)
    textInputpromp.setStyle("bold")
    textInputpromp.draw(win)
    
    milesEntry=Entry(Point(25,30),9)
    milesEntry.setFill("white")
    milesEntry.setSize(20)
    milesEntry.setTextColor("red")
    milesEntry.draw(win)
    
    milesEntrytxt=Text(Point(36,30),"Mile(s)")
    milesEntrytxt.setTextColor("Yellow")
    milesEntrytxt.setSize(28)
    milesEntrytxt.setStyle("bold")
    milesEntrytxt.draw(win)
    
    #set miles entered as an int and a str for later use
    win.getMouse()
    milesEntered =eval(milesEntry.getText())
    Miles=str(milesEntered)
    

#Information about Miles to Kilometers
#
#

    for thing in [textInputpromp, milesEntry, milesEntrytxt, nextSteptxt2]:
        thing.undraw()

    kmConvertxt1=Text(Point(10,36.75),"DID YOU KNOW?:")
    kmConvertxt1.setTextColor("Yellow")
    kmConvertxt1.setSize(20)
    kmConvertxt1.setStyle("bold")
    kmConvertxt1.draw(win)
    
    kmConvertxt2=Text(Point(30,32.5),"THERE ARE APPROXIMATELY 1.609344 "
                      "KILOMETERS PER MILE.")
    kmConvertxt2.setTextColor("Yellow")
    kmConvertxt2.setSize(19)
    kmConvertxt2.setStyle("bold")
    kmConvertxt2.draw(win)
    
    nextSteptxt3=Text(Point(30,7.5),"Results")
    nextSteptxt3.setTextColor("Yellow")
    nextSteptxt3.setSize(30)
    nextSteptxt3.setStyle("bold")
    nextSteptxt3.draw(win)
    #print(Miles)
#Show the convertion results
#
#
    #Undraw previous window
    win.getMouse()
    for thing2 in[kmConvertxt1, kmConvertxt2, nextSteptxt3, nextSteptxt1]:
        thing2.undraw()
    #Convertion and text for output       
    kiloConver=round(milesEntered* 1.609344,2)
    Kilometers = str(kiloConver)
    milestoKilotxt=Text(Point(30,36.75),("There are "+Kilometers+" kilometer(s) in "+Miles+" mile(s)."))
    milestoKilotxt.setSize(19)
    milestoKilotxt.setTextColor("Yellow")
    milestoKilotxt.draw(win)
    
    close1=Text(Point(30,12.5),"Click To")
    close1.setTextColor("Yellow")
    close1.setSize(30)
    close1.setStyle("bold")
    close1.draw(win)
    
    close2=Text(Point(30,7.5),"Quit")
    close2.setTextColor("Yellow")
    close2.setSize(30)
    close2.setStyle("bold")
    close2.draw(win)
    #Close window
    win.getMouse()
    win.close()

    

#My check in the Shell    
    #Miles=milesEntry.getText()
    #Kilometers = round(milesEntered * 1.609344,2)
    #print("There are", Kilometers,"Kilometer(s)", "in", milesEntered,"Mile(s).")
                        

 #WOW THIS WAS VERY INTERESTING TO WORK ON!!!!!!                       

main()
