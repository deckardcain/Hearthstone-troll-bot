def timeToTroll(): #defining the function
    wait("1408268382719.png", 130) #Waits for the turn to start - could be set to FOREVER but chose 130 for debug reasons
    sleep(76) #waiting time after turn has started. 90 seconds per round. Set to 76 so there's time to emote. Set this to 2 when testing and debugging
    rightClick("1408290095000.png") #Change this is you want to use another hero. 
    click("1408290113490.png") #GREETINGS 
    if exists("1408290170404.png"): #this is a stupid fix to the green button at turn one. Checks if the button is yellow or green - either way it's gonna press the button
        click("1408290181125.png")
    else:
        click("1408290200295.png")
    sleep(10) #wait ten seconds.    

while 2 > 1: #infinite loop unless math gets redefined by God.
    timeToTroll() #call the troll function
