#This program will Rick Roll the user ;) Whatta loser
#Read the questions and answer "Yes" or "No" accordingly
#Created by: Clare Groninger and Amber Beymer
def greeting():
    print("Hello there")

def askName():
    name = input("What is your name? ")
    print(name + " is a nice name!")
    askGive()
    
def askGive():
    print("\033[1;32;40m   \n")
    print("Are you ever gonna give me up?")
    print("\033[1;37;40m    \033 \n")
    give = input("PPlease type 'Yes' or 'No': ")
    if (give == "yes" or give == "Yes"):
      askRDown()
    elif(give == "no" or give == "No"):
      askEDown() #Redirects to next decision
    else:
      print("\033[1;31;40m    \033 \n")
      print ("II did not understand your response")
      askGive() #If the user responds incorrectly, they will have to reanswer
      
      #Yes responses correspond with "Really"
      #No responses correspond with "Ever"
      
   
def askEDown():
    print("\033[1;32;40m   \n")
    print("Are you ever gonna let me down?")
    print("\033[1;37;40m    \033 \n")
    EDown = input("PPlease type 'Yes' or 'No: ") #The two P's are intentional 
    if (EDown == "Yes" or EDown == "yes"):
      askRRun()
    elif (EDown == "No" or EDown == "no"):
      askERun()
    else:
      print("\033[1;31;40m    \033 \n")
      print("II did not understand your response") #The two I's are also intentional
      askEDown()
      
      
def askERun():
    print("\033[1;32;40m   \n")
    print("Are you ever gonna run around and desert me?")
    print("\033[1;37;40m    \033 \n")
    ERun = input("PPlease type 'Yes' or 'No': ")
    if (ERun == "Yes" or ERun == "yes"):
       askRCry()
    elif (ERun == "No" or ERun == "no"):
       askECry()
    else:
      print("\033[1;31;40m    \033 \n")
      print("II did not understand your response")
      askERun()
    
def askECry():
    print("\033[1;32;40m   \n")
    print("Are you ever gonna make me cry?")
    print("\033[1;37;40m    \033 \n")
    ECry = input("PPlease type 'Yes' or 'No': ")
    if (ECry == "Yes" or ECry == "yes"):
       askRBye()
    elif (ECry == "No" or ECry == "no"):
       askEBye()
    else:
      print("\033[1;31;40m    \033 \n")
      print("II did not understand your response")
      askECry()

def askEBye():
    print("\033[1;32;40m   \n")
    print("Are you ever gonna say goodbye?")
    print("\033[1;37;40m    \033 \n")
    EBye = input("PPlease type 'Yes' or 'No': ")
    if (EBye == "yes" or EBye == "Yes"):
      askRLie()
    elif(EBye == "no" or EBye == "No"):
      askELie()
    else:
      print("\033[1;31;40m    \033 \n")
      print ("II did not understand your response")
      askRBye()
  
    
  #This is the last decision that leads to the end  
def askELie():
    print("\033[1;32;40m   \n")
    ELie = input("Are you ever gonna tell me a lie and hurt me? ")
    if ("No" or "no"):
      print("\033[1;32;40m   \n")
      print ("You got Rick Roll'd ;)")
    elif(RLie == "Yes" or RLie == "yes"):
      print("\033[1;33;40m    \n")
      print ("I guess I'm the one Rick Roll'd :(")
    else:
      print("\033[1;31;40m    \033 \n")
      print ("II did not understand your response")
      askRLie()
    

def askRDown():
    print("\033[1;32;40m   \n")
    print("Are you realyy gonna let me down?")
    print("\033[1;37;40m    \033 \n")
    Down = input("PPlease type 'Yes' or 'No: ")
    if (Down == "Yes" or Down == "yes"):
      askRRun()
    elif (Down == "No" or Down == "no"):
      askERun()
    else:
      print("\033[1;31;40m    \033 \n")
      print("II did not understand your response")
      askRDown()


def askRRun():
    print("\033[1;32;40m   \n")
    print("Are you really gonna run around and desert me? ")
    print("\033[1;37;40m    \033 \n")
    Run = input("PPlease type 'Yes' or 'No': ")
    if (Run == "yes" or Run == "Yes"):
       askRCry()
    elif(Run == "no" or Run == "No"):
      askECry()
    else:
      print("\033[1;31;40m    \033 \n")
      print ("II did not understand your response")
      askRRun()
  
    

def askRCry():
    print("\033[1;32;40m   \n")
    print("Are you really gonna make me cry?")
    print("\033[1;37;40m    \033 \n")
    Cry = input("PPlease type 'Yes' or 'No': ")
    if (Cry == "yes" or Cry == "Yes"):
       askRBye()
    elif(Cry == "no" or Cry == "No"):
      askEBye()
    else:
      print("\033[1;31;40m    \033 \n")
      print ("II did not understand your response")
      askRCry()
  
    
def askRBye():
    print("\033[1;32;40m   \n")
    print("Are you really gonna say goodbye?")
    print("\033[1;37;40m    \033 \n")
    Bye = input("PPlease type 'Yes' or 'No': ")
    if (Bye == "yes" or Bye == "Yes"):
      askRLie()
    elif(Bye == "no" or Bye == "No"):
      askELie()
    else:
      print("\033[1;31;40m    \033 \n")
      print ("II did not understand your response")
      askRLie()
      
  #This is the other last decision that also leads to the end
def askRLie():
    print("\033[1;32;40m   \n")
    RLie = input("Are you really gonna tell me a lie and hurt me? ")
    if (RLie == "No" or RLie =="no"):
      print("\033[1;33;40m    \n")
      print ("You got Rick Roll'd ;)")
    elif(RLie == "Yes" or RLie == "yes"):
      print("\033[1;33;40m    \n")
      print ("I guess I'm the one Rick Roll'd :(")
    else:
      print("\033[1;31;40m    \033 \n")
      print ("II did not understand your response")
      askRLie()

    
    
    
greeting()
a = askName() 

c = askGive
  




