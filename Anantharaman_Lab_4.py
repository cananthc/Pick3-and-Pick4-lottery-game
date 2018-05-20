#############################################################################
# Author     : Anantharaman Chandar                                         #
# CWID       : A20403439                                                    #
# Course     : ITMD 513 Open Source Programming Lab4                        #
# Instructor : James Papademas                                              #
# Description: Lottery Prediction with Fireball                             #
#                                                                           #
#                                                                           #
#                                                                           #
#############################################################################
import random,sys,datetime

lotteryNum=list()
userLot = list()
LotTemp = list()
fireBall = list()

##Choice Initiator
def welcomeMethod():
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M"))
    print("Programmed by Anantharaman Chandar")
    print()
    print("Welcome to Illinois Lottery Center\n")
    print("Enter 1 for Pick 3 Lotto without FireBall: ")
    print("Enter 2 for Pick 4 Lotto without FireBall: ")
    print("Enter 3 for Pick 3 Lotto with Fireball   : ")
    print("Enter 4 for Pick 4 Lotto with Fireball   : ")
    
    try: 
        choice= int(input())

        ## Pick 3 Lotto game without FireBall
        if choice ==1:
                print("Playing Pick 3 Lotto........")
                generateLotteryNumber(3) #Generate 3 random Numbers
                print()
                for i in range(0,3): #Give user 3 tries
                    userInputNumber(3) #Get 3 Numbers from User
                    checkWinnerWithoutFireBall(lotteryNum,userLot,i) #Check if User is a winner
                    #Clear user's  Lottery number and get a new Lottery Number
                    del userLot[:]
                    del LotTemp[:]
                
        ## Pick 4 Lotto game without FireBall
        elif choice ==2:
            print("Playing Pick 4 Lotto........")
            generateLotteryNumber(4) #Generate 4 random Numbers
            print()
            for i in range(0,3): #Give user 3 tries
                userInputNumber(4) #Get 4 Numbers from User
                print()
                checkWinnerWithoutFireBall(lotteryNum,userLot,i) #Check if User is a winner
                #Clear user's  Lottery number and get a new Lottery Number
                del userLot[:]
                del LotTemp[:]


        ## Pick 3 Lotto game with FireBall
        elif choice ==3:
            print("Playing Pick 3 Lotto with Fireball.........")
            generateLotteryNumber(3) #Generate 3 random Numbers
            print()
            generateFireballNumber()#Generate 1 random Number for FireBall
            print()
            for i in range(0,3): #Give user 3 tries
                userInputNumber(3) #Get 3 Numbers from User
                #print(i)
                checkWinnerWithFireBall(lotteryNum,userLot,fireBall,3,i)
                #Clear user's  Lottery number and get a new Lottery Number
                del userLot[:]
                del LotTemp[:]


        ## Pick 4 Lotto game with FireBall
        elif choice ==4:
            print("Playing Pick 4 Lotto with Fireball........")
            generateLotteryNumber(4) #Generate 4 random Numbers
            print()
            generateFireballNumber() #Generate 1 random Number for FireBall
            print()
            for i in range(0,3): #Give user 3 tries
                userInputNumber(4)
                print()
                print()
                checkWinnerWithFireBall(lotteryNum,userLot,fireBall,4,i)
                #Clear user's  Lottery number and get a new Lottery Number
                del userLot[:]
                del LotTemp[:]
                
        else:
            print("Oops... Sorry the Entered Choice is Invalid")
            
    except ValueError:
        print("Invalid Literal...Program will Exit Now")

#Generate Lottery Number and append to a List    
def generateLotteryNumber(x):
    for i in range(0,x):
        lotteryNum.append(random.randint(0,9))
    #print(lotteryNum)

#Generate FireBall Number and append to a List  
def generateFireballNumber():
    fireballNum = random.randint(0,9)
    fireBall.append(fireballNum)
    #print(fireBall)
    return fireBall

#Get Users Lottery Number one by one
def userInputNumber(x):
    for i in range(0,x):
        userNum = int(input("Enter Your Lottery Numbers one by one: "))
        if userNum >= 0 and userNum < 10:
            userLot.append(userNum)
        else:
            print("Number can be from 0 to 9 only. Please try again.")
            sys.exit()
        
    print("Your Lottery  Number is: ",userLot)
    print()
        
        
#Check if the users Lottery Number matches the generated Lottery Number without FireBall        
def checkWinnerWithoutFireBall(lotteryNum,userLot,i):
    if(lotteryNum == userLot):
        print("Congrats You are a Winner.......")
        print("Todays LotteryNum                ",lotteryNum)
        print("User Lottery Number              ",userLot)
        print("Your Total Prize Amount is $100.........")
        print()
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M"))
        print("Programmed by Anantharaman Chandar")
        
        sys.exit()
    else:
        print("That was Close.... But, Sorry You Lost....")
        #print(i)
        if i in(0,1):
            print("Enter 1 to try again..")
            print("Enter 2 to exit and see the Lottery Number........")
            try:
                option=int(input())
                if option==2:
                    print("Todays LotteryNum                ",lotteryNum)
                    print("User Lottery Number              ",userLot)
                    now = datetime.datetime.now()
                    print(now.strftime("%Y-%m-%d %H:%M"))
                    print("Programmed by Anantharaman Chandar")
                    sys.exit()
                elif option==1:
                    pass
                else:

                    print("Invalid Choice.....Program will Exit")
                    sys.exit()
                    
            except ValueError:
                print("Value Error")
                
        if i ==2:
            print("Todays LotteryNum                ",lotteryNum)
            print("User Lottery Number              ",userLot)
            now = datetime.datetime.now()
            print(now.strftime("%Y-%m-%d %H:%M"))
            print("Programmed by Anantharaman Chandar")



#Check if the users Lottery Number matches the generated Lottery Number with FireBall
def checkWinnerWithFireBall(lotteryNum,userLot,fireBall,x,i):
    #print("Todays Lottery Number            ",lotteryNum)
    #print("User Lottery Number              ",userLot)
    #print("FireBall Number                  ",fireBall)
    #print(i)
    for x in range(0,x):
            LotTemp.append(lotteryNum[x])
    if(lotteryNum == userLot):
        print("Congrats You Are a Winner......")
        print("Todays Lottery Number            ",lotteryNum)
        print("User Lottery Number              ",userLot)
        print("FireBall Number                  ",fireBall)
        bonusFireBallCheck(lotteryNum,userLot,fireBall,LotTemp,x,i)
        
        
        
    else:
        print()
        print("Sorry You Lost...... Checking if you are winner with FireBall")
        
        #print(userLotTemp)
        fireBallCheck(lotteryNum,userLot,fireBall,LotTemp,x,i)

#Check if the users Lottery Number matches the generated Lottery Number with FireBall as a WildCard  
def fireBallCheck(lotteryNum,userLot,fireBall,LotTemp,x,i):
    #Iterate each list values with WildCard to check for combinations
    #print("i Value is",i)
    #print(x)
    #print(LotTemp)
    for a in range(0,x+1):
        lotteryNum[a]=fireBall[0]
        #print(lotteryNum)
        if lotteryNum == userLot:
            Status=0
            break
        else:
            lotteryNum[a]=LotTemp[a]
            Status=1
        #print(LotTemp)
    #print("Status is",Status)
    print()
    
    if Status ==0:
        print("Congrats You are a Winner with FireBall........")
        print("Your Original Lottery Number      ",userLot)
        print("Actual Lottry Number              ",LotTemp)
        print("Winning Lottery Num               ",lotteryNum)
        print("FireBall Number                   ", fireBall)
        print("Your Total Prize Amount is $100.........")
        print()
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M"))
        print("Programmed by Anantharaman Chandar")
        sys.exit()
    else:
        if Status ==1:
            #print("len value is",x)
            print("That Was Close........ Better luck Next Time")
            #print(i)
            if i in (0,1):
                print("Enter 1 to try again..")
                print("Enter 2 to exit and see the Lottery Number........")
                try:
                    option=int(input())
                    if option==2:
                        print("Your Original Lottery Number      ",userLot)
                        #print("User Lottery Number with FireBall ",userLot)
                        print("Winning Lottery Num               ",lotteryNum)
                        print("FireBall Number                   ", fireBall)
                        print("Your Total Prize Amount is $0.00........")
                        sys.exit()
                    elif option==1:
                            pass
                except ValueError:
                    print("Invalid Literal....Program will exit now")
                    sys.exit()
            

            if x==2 and i==2:
                print("Your Original Lottery Number      ",userLot)
                #print("User Lottery Number with FireBall ",userLot)
                print("Actual Lottry Number              ",LotTemp)
                print("Winning Lottery Num               ",lotteryNum)
                print("FireBall Number                   ", fireBall)
                print("Your Total Prize Amount is $0.00........")
                now = datetime.datetime.now()
                print(now.strftime("%Y-%m-%d %H:%M"))
                print("Programmed by Anantharaman Chandar")
            if x==3 and i==2:
                print("Your Original Lottery Number      ",userLot)
                #print("User Lottery Number with FireBall ",userLot)
                print("Winning Lottery Num               ",lotteryNum)
                print("FireBall Number                   ", fireBall)
                print("Your Total Prize Amount is $0.00........")
                now = datetime.datetime.now()
                print(now.strftime("%Y-%m-%d %H:%M"))
                print("Programmed by Anantharaman Chandar")
                
def bonusFireBallCheck(lotteryNum,userLot,fireBall,LotTemp,x,i):
    print()
    print("Additional Prize Money Checker")
    for a in range(0,x+1):
        lotteryNum[a]=fireBall[0]
        #print(lotteryNum)
        if lotteryNum == userLot:
            Status=0
            break
        else:
            lotteryNum[a]=LotTemp[a]
            Status=1
        #print(LotTemp)
    #print("Status is",Status)
    
    if Status ==0:
        print("Congrats You Won Extra $50")
        print("Your Total Prize Amount is $150.00......")
        print()
        
    else:
        print()
        print("Sorry No additional Prize")
        print("Your Total Prize Amount is $100.........")
        print()
        
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M"))
    print("Programmed by Anantharaman Chandar")
    sys.exit()
    
##Initiate the program
welcomeMethod()
    
    
