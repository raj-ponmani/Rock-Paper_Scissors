import time
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty("voices")

engine.setProperty("voice",voices[2].id)

engine.setProperty("rate",170)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def user_command_input():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("listening...")
            whatUsaid = listener.listen(source)
            print("got it")
            command = listener.recognize_google(whatUsaid)
            command = command.lower()
            print(command)
    except:
        ex = print('can not recognise what you said please talk again...')
        print(ex)
        talk(ex)
    return command
welcome = "welcome to rock paper scissors game"
raj = "Made by RAJ"
print(welcome)
talk(welcome)
print(raj)
talk(raj)

loose = ("the computer wins")
win = ("you win")
lives = 5
score =0
drew = 0
computer_lives = 7
password_list = []
while True:
    account = "To begin fill in the follow information:  "
    print(account)
    talk(account)
    talk("please enter your username:  ")
    username = input("please enter your username:  ")
    talk("please enter your password:  ")
    password = input("please enter your password:  ")
    searchfiles = open("accounts.txt","r")
    for line in searchfiles:
        password_list.append(line.strip())
        if username and password in password_list:
            print("access granted")
            talk("access granted")
            time.sleep(0.5)
            print("loading...")
            time.sleep(0.5)
            print("loading...")
            time.sleep(0.5)
            print("loading...")
            time.sleep(0.5)
            start_menu = """
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     ___                  ______________     ______________     _______________     ____      ___                                            
    ¦   ¦                ¦              ¦   ¦              ¦   ¦               ¦   ¦    ¦    /   /                                           
 /------------------     ¦     ___      ¦   ¦  __________  ¦   ¦  _____________¦   ¦    ¦   /   /                                            
/            \     ¦     ¦    ¦   ¦     ¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦  /   /                                             
¦       ------------     ¦    ¦___¦   __¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦_/   /                                              
¦       ------------     ¦           \      ¦ ¦          ¦ ¦   ¦ ¦                 ¦         /                                               
¦            \     ¦     ¦    ¦\      \     ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦\   \                                               
¦       ------------     ¦    ¦ \      \    ¦ ¦__________¦ ¦   ¦ ¦_____________    ¦    ¦ \   \                                              
¦       ------------     ¦    ¦  \      \   ¦              ¦   ¦               ¦   ¦    ¦  \   \                   ___  ___  ___  ___    
¦            \     ¦     ¦____¦   \______\  ¦______________¦   ¦_______________¦   ¦____¦   \___\                 ¦   ¦¦   ¦¦   ¦¦   ¦       
¦       ------------                                                                                          ___ ¦   ¦¦   ¦¦   ¦¦   ¦       
\       ------------ ___________     _______________     ___________     ___________     _____________       ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
 \           \     /¦   _____   ¦   ¦     _____     ¦   ¦   _____   ¦   ¦           ¦   ¦             ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
  \---------------/ ¦  ¦     ¦  ¦   ¦    ¦_____¦    ¦   ¦  ¦     ¦  ¦   ¦    _______¦   ¦     ___     ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
                    ¦  ¦_____¦  ¦   ¦     _____     ¦   ¦  ¦_____¦  ¦   ¦   ¦           ¦    ¦   ¦    ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
                    ¦    _______¦   ¦    ¦     ¦    ¦   ¦    _______¦   ¦   ¦_____      ¦    ¦___¦   _¦      \                       /       
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦    _____¦     ¦           \         \                     /        
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦   ¦_______    ¦    ¦\      \         \                   /         
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦           ¦   ¦    ¦ \      \         \                 /                                _____
                    ¦___¦           ¦____¦     ¦____¦   ¦___¦           ¦___________¦   ¦____¦  \______\         \_______________/                                /     /
                                                                                                                                                                 /     /
 ______________     _______________     ____     ______________     ______________     ______________     _____________     ______________                    /     /
¦   ___________¦   ¦               ¦   ¦    ¦   ¦   ___________¦   ¦   ___________¦   ¦              ¦   ¦             ¦   ¦   ___________¦    ________    /     /
¦  ¦               ¦  _____________¦   ¦    ¦   ¦  ¦               ¦  ¦               ¦  __________  ¦   ¦     ___     ¦   ¦  ¦               /          /     /
¦  ¦___________    ¦ ¦                 ¦    ¦   ¦  ¦___________    ¦  ¦___________    ¦ ¦          ¦ ¦   ¦    ¦   ¦    ¦   ¦  ¦___________   ¦         /     /
¦____________  ¦   ¦ ¦                 ¦    ¦   ¦____________  ¦   ¦____________  ¦   ¦ ¦          ¦ ¦   ¦    ¦___¦   _¦   ¦____________  ¦  ¦       /     /
             ¦ ¦   ¦ ¦                 ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦          ¦ ¦   ¦           \                  ¦ ¦  ¦               __________________
             ¦ ¦   ¦ ¦_____________    ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦__________¦ ¦   ¦    ¦\      \                 ¦ ¦  ¦                                 ¦
 ____________¦ ¦   ¦               ¦   ¦    ¦    ____________¦ ¦    ____________¦ ¦   ¦              ¦   ¦    ¦ \      \    ____________¦ ¦  ¦               __________________¦
¦______________¦   ¦_______________¦   ¦____¦   ¦______________¦   ¦______________¦   ¦______________¦   ¦____¦  \______\  ¦______________¦  ¦______________¦

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Live Rules
You start with 5 lives.
If you win you get a extra live.
If you loose you loose a live.
If you draw the lives stay the same.
-----------------------------------------
To see a list of rules type rules.
-----------------------------------------
At any point type exit to leave the game.
-----------------------------------------
The computer has lives aswell.
Can you beat the computer?
Good Luck!!
-----------------------------------------
"""
            print(start_menu)
            talk("Can you beat the computer? Good Luck!!")
            while True:
                rps = "rock,paper,scissors?  "
                print(rps)
                talk(rps)
                rps = user_command_input()
                rps = rps.title()
                rps = rps.lower()
                import random
                computer = ("rock","paper","scissors")
                computer = random.choice(computer)
                #rock if statement
                if "rock" in rps and computer == "paper":
                    print("the computer choose",computer)
                    print("")
                    print(loose)
                    talk(loose)
                    print("")
                    print("")
                    lives-=1
                if rps == "rock" and computer == "scissors":
                    print("the computer choose", computer)
                    print("")
                    print(win)
                    talk(win)
                    computer_lives -= 1
                    print("")
                    print("")
                    score+=1
                #paper if statements
                if rps == "paper" and computer == "rock":
                    print("the computer choose", computer)
                    print("")
                    print(win)
                    talk(win)
                    computer_lives -= 1
                    print("")
                    print("")
                    score += 1
                if rps == "paper" and computer == "scissors":
                    print("the computer choose", computer)
                    print("")
                    print(loose)
                    talk(loose)
                    print("")
                    print("")
                    lives -= 1
                #Scissors if statement
                if rps == "scissors" and computer == "rock":
                    print("the computer choose", computer)
                    print("")
                    print(loose)
                    talk(loose)
                    print("")
                    print("")
                    lives -= 1
                if rps == "scissors" and computer == "paper":
                    print("the computer choose", computer)
                    print("")
                    print(win)
                    talk(win)
                    computer_lives -= 1
                    print("")
                    print("")
                    score += 1
                #duplicate if statement
                if rps == "rock" and computer == "rock":
                    print("the computer choose", computer)
                    print("")
                    print("you drew")
                    talk("you drew")
                    print("")
                    print("")
                    drew += 1
                if rps == "paper" and computer == "paper":
                    print("the computer choose", computer)
                    print("")
                    print("you drew")
                    talk("you drew")
                    print("")
                    print("")
                    drew += 1
                if rps == "scissors" and computer == "scissors":
                    print("the computer choose", computer)
                    print("")
                    print("you drew")
                    talk("you drew")
                    print("")
                    print("")
                    drew += 1
                #system
                if rps == "rules":
                    print("**********************************************")
                    print("Rules")
                    print("**********************************************")
                    print("-Rock looses against Paper")
                    print("-Rock beats Scissors")
                    print("-Paper beats Rock")
                    print("-Paper looses against Scissors")
                    print("-Scissors beats Paper")
                    print("-Scissors looses against Rock")
                    print("**********************************************")
                if rps == "display lives":
                    print("you have " + lives + "lives")
                    talk("you have " + lives + "lives")
                if rps == "display score":
                    print("your score is " + score)
                if rps == "display drew":
                    print("you have " + drew + "drew matches")
                #lives
                if lives == 0 or rps == "test":
                    print("Thanks for playing...")
                    talk("Thanks for playing...")
                    print("You have ran out of lives")
                    talk("You have ran out of lives")
                    print("You got",score,"correct")
                    talk("You got" + score + "correct")
                    print("drew",drew,"times")
                    talk("drew" + drew + "times")
                    stop =input("press enter to exit")
                    exit()
                if computer_lives == 0 or rps == "test":
                    print("Thanks for playing...")
                    talk("Thanks for playing...")
                    print("The computer lost all its  lives")
                    talk("The computer lost all its  lives")
                    print("You got",score,"correct")
                    talk("You got"+score+"correct")
                    print("drew",drew,"times")
                    talk("drew"+drew+"times")
                    stop =input("press enter to exit")
                    exit()
                #exit
                if rps == "exit":
                    break
                else:
                    pass
            if password in line and password != line:
                print("Your username or password is incorrect.")
                print("---------------------------------------")

            else:
                print("please say again")
                talk("please say again")