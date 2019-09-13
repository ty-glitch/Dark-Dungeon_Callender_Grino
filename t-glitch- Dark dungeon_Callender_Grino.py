"""
This is a dungeon choose you own adventure
"""
import time 
import sys
# THIS ALLOWS TEXT TO APPEAR ON SCREEN ONE AT A TIME
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.07)
# THIS FUNCTION GIVES THE FIRST CHOICE TO MAKE
def firstchoice():
  time.sleep(3)
  delay_print("\nThe great dungeon stands before you, now it's time to make a decision, " + theName + ".")
  time.sleep(3)
  delay_print("\nDo you walk in to this vast dungeon or do you run away?\n Walk (w) or Run (r)?\n")
  ans1=input()

# THIS FUNCTION GIVES THE SECOND OPION TO MAKE
  if ans1== "w":
    time.sleep(2)
    delay_print("You walked down a dark hallway ")
    time.sleep(2)
    delay_print("You come to a fork, with two equally dark pathways")
    time.sleep(2)
    delay_print("Do you choose: The left path (l) or The right path(r)? \n")
    leftRight=input()
    if leftRight== "r":
      minoTaur()
    elif leftRight=="l":
      quickSand()
    else:
      time.sleep(2)
      delay_print("Think you're clever?, Stick to the options given, please")
     
     
 




  elif ans1== "r":
    time.sleep(2)
    delay_print("Oh, " +theName +", " +theName +", "+theName+ ", " + "you coward. You think you've gotten away, but the ground falls out underneath you")
    time.sleep(2)
    delay_print ("You fall into a spider web it breaks your fall but the spider sees you and scurries over." )
    spiderChoice()

  


# DEFAULT ACTION IN CASE PLAYER DOESNT STICK TO OPTIONS
  else:
    delay_print("Think you're clever?, Stick to the options given, please")
    firstchoice()


def spiderChoice():
  time.sleep(2)
  delay_print("You struggle your way out of the web, and in the corner of the room you spot a chest full of loot\n Do you:")
  delay_print("Fight for the loot(f) or Run for your life(r)?\n")
  ans2=input()




  if ans2=="f":
    delay_print("You punch the spider in the face")
    time.sleep(1)
    delay_print("kapoww,Kablam")
    time.sleep(1)
    delay_print("The spider screeches with pain and limps away")
    winGame()



  elif ans2=="r":
    time.sleep(1)
    delay_print("You run, hoping to come back for the loot later.")
    time.sleep(2)
    delay_print("After escaping in to a cramped, dark crawlspace, you quickly become lost in the many winding passages")
    time.sleep(2)
    delay_print("You crawl and crawl... but the way out seemingly doesn't exist, and you soon forget the way you came ")
    time.sleep(2)
    delay_print("Eventually, exhaustion, starvation and thirst set in.")
    time.sleep(2)
    delay_print("The world fades...")
    loseGame()
    




  else:
    time.sleep(2)
    delay_print("Think you're clever?, Stick to the options given, please")

def quickSand():
  time.sleep(2)
  delay_print("You proceed down the left passage, and as you walk, you realize the ground is soft, and getting softer and softer, and walking is getting progressively more difficult")
  time.sleep(2)
  delay_print("It's muhfkn quicksand")
  time.sleep(1)
  delay_print("You struggle and struggle to escape, but you only sink deeper")
  loseGame()

  
def minoTaur():
  delay_print('This passsage is espcially dark, through squinting eyes you see a human like figure emerging from the darkness.\nAs it comes closer you make-out the legs of a bull. Oh God!!. its a Minotuar!!!!!!!! \nIt starts to charge at you')
  loseGame()
 
def winGame():
  delay_print("you leave the dungeon stacked with $$$")
  delay_print("YOU WIN")
  
def loseGame():
  delay_print("YOU DIE")



# this is the greeting
delay_print("Greetings! Welcome to a DARK DUNGEON.")
delay_print(" What is your name?\n")
theName=input() 
delay_print (theName + " ,huh? Haven't heard that one before...Anyway let's go!")
firstchoice()




