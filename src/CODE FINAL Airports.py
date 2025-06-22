#The Code

#LIBRARIES
import csv
import os
from idlecolors import *

#Welcome header
print("**********************************************")
for i in range(0,2):
    print("**                                          **")
print("   WELCOME TO THE FILGHT PLANNING PROGRAM     ")
for i in range(0,2):
    print("**                                          **")
print("**********************************************")

#Files, Arrays and Global variables
filename = "Airports.txt"
EntryDB = {} #library for storing the user's data

StdSeats = 0
FstSeats = 0
Dist2AP = 0
User_Opt = 0
act = []
CostPerSeat = 0
FullOVAP = ""
FullUKAP = ""
found = 0
OVAP = ""
UKAP = ""

UserEntryList = [0,0,0,0,0,0,0,0] #This list will be updated and will store the user's information

########

#SUBROUTINE TO OPEN AND READ A FILE
def RFiles(filename): #the value that called this subroutine is put in the parameter 'filename'
    with open(filename, newline='') as myfile: #opens and reads the file + stores it with the filename 'myfile'
        rows = csv.reader(myfile, delimiter=',') #passes my csv file into the 'csv reader method' which by default/already built in
                                                 #the reader method already knows the format of a csv file(seperated by commas...etc)
                                                 #the data is then stored in a 2D array called rows
        for row in rows: #prints out each array in the 2D array
            print("  ",row) #each array will be printed after a space

########

#SUBROUTINE TO CHECK DATA OF AIRCRAFT ENTERED
def DispACT(filename): #Displays the aircraft
    with open(filename, newline='') as anyfile:
        rows = csv.reader(anyfile, delimiter=',') #creates 2D array called 'rows'
        global act
        act = [] #creates an array called act
        data1 = [] #array called data1
        for row in rows: #for each array in 'rows'
            data1.append(row) #it is added in the 2D array called data1
        global UserEntryList
        for item in data1: #checks if the first value in every array in 'data1' is equal to the initials(uppercase) of the Aircraft
            if item[0] == AirCft.upper():
                act = item #stores the array containing only the data about the users chosen aircraft in the variable, 'act'
                #print("Details of the aircraft type entered:",act) #displays details of the entered aircraft
                printc(purple("Details of the aircraft chosen:\n"))
                print("     TYPE OF AIRCRAFT:",act[1])
                print("     RUNNING COST PER SEAT / 100KM:",act[2])
                print("     MAXIMUM FLIGHT RANGE:",act[3],"KM")
                print("     CAPACITY IF ALL SEATS ARE STANDARD-CLASS:",act[4])
                print("     MINIMUM NUMBER OF FIRST-CLASS SEATS:",act[5])
        return

########

#SUBROUTINE TO CHECK THE VALIDITY OF THE OVERSEAS AIRPORT CODE
def CheckOAP(ffile): #Checking the Overseas Airport
    with open(ffile, newline='') as myfile: #reads, opens the OAP file and renames it 'ffile'
        rows = csv.reader(myfile, delimiter=',') 
        data = []
        for row in rows:
            data.append(row) #appends each row from the 2D array 'rows' to the 2D array 'data'
    global found
    global Dist2AP
    global FullOVAP
    global FullUKAP
    global UserEntryList
    global act
    global OVAP
    global UKAP

    for item in data: #for each array stored in the 2D array 'data'
        str1 = item[0] #the variable str1 stores the 1st value of that array which is the initials of the overseas airport(which is in uppercase)
        str2 = OVAP.upper() #str2 stores the uppercase(the same as str1)

        if str1==str2: #if they are both equal then the following code runs
            found=1 #dummy variable
            print(" ")
            print("Valid code")
            print("The Overseas Airport chosen is:",item[1]) #prints the full name of the Overseas Airport

            FullOVAP=item[1] #stores the full name of the Overseas Airport in the variable FullOVAP
            UserEntryList[1] = OVAP.upper() + FullOVAP #the initials and full name of the OVAP is stored as the second value UserEntryList array
            print(item)

            #finds the distance between both the overseas and UK airport + stores it in the UserEntryList
            if UKAP.upper() == "LJL":
                Dist2AP = item[2] #finds the Distance between 2 airports
                FullUKAP = "Liverpool John Lennon" #stores the full name of the UK airport as FullUKAP
                UserEntryList[0] = UKAP.upper() + FullUKAP #adds both the names to the list
                UserEntryList[2] = Dist2AP #adds the distance to the list
                #print("SS",Dist2AP)
            elif UKAP.upper() == "BMI": #same as above but for BMI
                Dist2AP = item[2]
                FullUKAP = "Bournemouth International"
                UserEntryList[0] = UKAP.upper() + FullUKAP
                UserEntryList[2] = Dist2AP
            #print("SS",Dist2AP)

#######

#SUBROUTINE TO CALCULATE THE AMOUNT OF STANDARD SEATS
def Cal_StdSeat(): #Calculating number of Standard Class Seats
    #print("inside cal_std",act[4])
    global StdSeats
    global UserEntryList
    global FstSeats
    StdSeats = int(act[4]) - (FstSeats*2) #capacity if all seats are standard class - number of first class seats x 2
    UserEntryList[5] = StdSeats #stores the amount of standard class seats in the UserEntryList
    #print("inside cal_std2,",StdSeats)
    #print(UserEntryList)
    return StdSeats

#######

#SUBROUTINE TO SAVE THE OUTPUT AS THE DETAILS ARE BEING ENTERED EVERY QUESTION
def Savedata(somestr):
    EntryDB.update(somestr) #updates the values entered into the library EntryDB
    #print(EntryDB)
    f = open("myfile.txt","w+") #writes the values to the library
    f.write(str(EntryDB)) #converts all data to be strings
    f.close()

#######

#SUBROUTINE TO PRINT AN ERROR MESSAGE
def Error_Message():
    print("INVALID AIRPORT CODE!")

#######

def inputOption(message):
    while True:
        try:
            Opt_Value = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return Opt_Value
            break

#######

#4 - Choice 1: Airport Details
def AirportDetails():
    print(" ")
    printc(green("You have chosen to enter Airport Details.\n"))

    #UK Airport
    RFiles("UKAirports.txt") #calls the subroutine RFiles to open, read and display the csv file: Airports.txt
    global UKAP
    global OVAP
    global Dist2AP
    global found
    global FullUKAP
    global FullOVAP

    try: 
        print(" ")
        UKAP = input("Please enter the three letter UK Airport Code (Refer Above): ")
    except:
        print("Please refer above for the 3 letter UK Airport Code: ") #if any error happens with the above code then this line will be printed

        
    #Is the UK Airport code valid?
    if UKAP.upper() == "LJL" or UKAP.upper() == "BMI": #accepts both uppercase and lowercase for answers
        val = "FALSE"
    else:
        val = "TRUE"
        while val == "TRUE":
            print("Invalid UK Airport Code. Please re-enter the code by choosing option 1-Airport details")
            main()
            if UKAP.upper() == "LJB" or UKAP.upper() == "BMI":
                val = "FALSE"

    print("You have chosen:",UKAP.upper()," as your UK Airport.")

    
    #Asks the User for the Overseas Airport Code
    print(" ")
    RFiles("OverseasAirports.txt") #again reads and opens the file for the overseas airport
    
    try: #error handling
        print(" ")
        OVAP = input("Please enter the three-letter Airport Code for the Overseas Airport (Refer Above): ") #this is what should be displayed to the user
    except: #in case if user input causes an error, then the following code should run
        print("Please refer above for the 3 letter Overseas Airport Code: ") #this line is displayed instead in case of an error


    #Is the Overseas Airport code valid?
    CheckOAP("OverseasAirports.txt") #sends it to check the Overseas Airport code
    while found == 0: 
        #print(OVAP.upper(),"inside while") 
        RFiles("OverseasAirports.txt")
        OVAP = input("Invalid Overseas Airport Code. Please refer above for the three letter codes: ")
        CheckOAP("OverseasAirports.txt")

    #prints out the entered information to the user
    print("\nYou have chosen:",OVAP.upper(),"-", FullOVAP, "as your Overseas Airport")
    print("You have chosen:",UKAP.upper(),"-", FullUKAP, "as your UK Airport")
    print("The distance between the two is",Dist2AP,"KM")

    str1={'UK Airport':UKAP.upper(),'Overseas Airport':OVAP.upper(),'Dist2AP':Dist2AP} #stores it in the library str1
    Savedata(str1) #sends str1 to the subroutine to save the data
    print(" ")

#########

#5 - Choice 2: Flight Details
def FlightDetails():
    print(" ")
    printc(purple("You have chosen to enter Flight Details.\n"))
    RFiles("AirCraftType.txt") #reads, opens and displays the file which stores info on Aircraft types for the user
    global FstSeats #first class seats
    global AirCft #aircraft
    global StdSeats #standard class seats


    FstSeats = 0
    ACtype = ["MN", "LN", "MW"] #array stores initials of the types of aircraft

    #error handling
    try:
        print(" ")
        print("Enter the type of Aircraft (refer below) ")
        AirCft = input("Please type   'MN' for a 'Medium Narrow Body Aircraft'\n              'LN' for a 'Large Narrow Body Aircraft'\n              'MW' for a 'Medium Wide Body Aircraft' : ");
    except:
        print("Please type Aircraft information and refer above.")
        
    #Is it valid? 
    ACtype = ["MN", "LN", "MW"]

    if AirCft.upper() in ACtype:
        print("Chosen Aircraft is",AirCft.upper())
        print(" ")
    else:
        print("Invalid type. Try again!")

    DispACT("AirCraftType.txt") #sends to subroutine to display the aircraft information for the user's choice


    #Entry for First Class Seats and Validating the data
    print(" ")
    FstSeats = inputOption("Please enter the number of First Class Seats: ")
    if FstSeats != 0:
        #print(act)
        cmp = int(act[5]) #retreiving the number of first class seats from the array 'act' whic contains data specific to the users chosen aircraft

        #code checks whether the user has entered a value which is less than the maximum number of FstSeats
        if FstSeats < cmp:
            print("You have entered less than the minimum number of first class seats for the chosen Aircraft!\n Please select Option 2-Flight details and re-enter.")
            
        else:
            global UserEntryList
            str2 = {'AirCraftType':AirCft}
            str3 = {'No_FirsTClas_Seat':FstSeats}
            UserEntryList[4] = FstSeats #saves it to the UserEntryList

            #saves the data entered
            Savedata(str2)
            Savedata(str3)
            StdSeats = Cal_StdSeat()
            #print("hiii",StdSeats)

    else:
        print("Invalid choice. Please select Option 2-Flight details and re-enter.")
    #print("NUMBER OF STANDARD CLASS SEATS:",StdSeats)

########

#SUBROUTINE TO CALCULATE THE FLIGHT COST PER SEAT
    #THE RUNNING COST PER SEAT PER 100KM
def FlightSeat_Cost():
    global UserEntryList
    global act
    global CostPerSeat
    global Flight_Cost

    #print(UserEntryList)

    if len(UserEntryList) != 0 and len(act) != 0:
        #print(act)
        #print(UserEntryList)
        #print(act[2])
        #print(UserEntryList[2])
        price = (act[2])
        #print(price)
        price = price.split("£")
        #print(price)
        #print(price[1])
        RCost100km = int(price[1])
        Dist2A = int(UserEntryList[2])

        CostPerSeat = RCost100km * Dist2A/100
        print("Flight cost per seat: £",CostPerSeat)

    else:
        print("Please enter the proper flight details and aircraft details by choosing option 1 and option 2")
        user_menu()

    PriceFstClass = inputOption("Please enter the price of First Class Tickets: £")
    UserEntryList[6] = PriceFstClass
    
    PriceStdClass = inputOption("Please enter the price of Standard Class Tickets: £")
    UserEntryList[7] = PriceStdClass

    #Flight Cost
    NoFirstClassSeat = int(UserEntryList[4])
    StdSeat = int(UserEntryList[5])
    print("Number of First Class Seats: ",NoFirstClassSeat)
    Flight_Cost = CostPerSeat * (NoFirstClassSeat + StdSeats)
    #print("Flight cost: £",Flight_Cost)

    #Flight Income
    Flight_Income = NoFirstClassSeat * PriceFstClass + StdSeats * PriceStdClass
    #print("Flight Income: £",Flight_Income)

    #Flight Profit
    Flight_Profit = Flight_Income - Flight_Cost
    #print("Flight Profit: £",Flight_Profit)

    #Appending all the calculated data to the UserEntryList
    UserEntryList.append(CostPerSeat)
    UserEntryList.append(Flight_Cost)
    UserEntryList.append(Flight_Income)
    UserEntryList.append(Flight_Profit)
    #print(UserEntryList)
    CalProfDisplay()

#########

#6 - Option 3
#this code ensures that all values have been entered to proceed with the calculations for the total flight cost
def CalProfCheck():
    global UserEntryList
    global Dist2AP
    global act

    printc(orange("You have chosen to enter the Price Plan and Calculate profit.\n"))
    #RFiles("myfile.txt") 
    if len(UserEntryList) == 0:
        print("Pleae enter the UK and the Overseas Airport Codes for the Price Plan and Profit Calculation.")
        print("Please select Option 1 in the main menu to do this.")
    elif len (UserEntryList) != 0:
        dummy1 = UserEntryList[0]
        dummy2 = UserEntryList[1]
        if dummy1 == "" or dummy2 == "":
            print("Please enter the codes for the Overseas Airport for the Price Plan and Profit Calculation")
            print("Please select Option 1 in the main menu to do this.")
            
    if len(act) == 0:
        print("Please enter the flight details to enter the Aircraft type and the number of first class seats required. This information in needed to calculate the profit and make a price plan.")
        print("To do this please select Option 2 in the main menu.")
        
    elif len(act) != 0:
        #print(len(act))
        maxflightdist = int(act[3])
        #print(Dist2AP,act[3])
        #print(UserEntryList)
        if maxflightdist < int(Dist2AP):
            print("Please select the appropriate Aircraft type by selecting option 2, make sure the maximum flight range(km) selected is more than the distance between the two airports.")
        else:
            FlightSeat_Cost()

#########

#Q6 - Option 3: Calculate the Profit and Enter the Price Plan
def CalProfDisplay(): #calls the subroutine to display the entered the price plan and calulated profit 
    global UserEntryList
    
    print(" ")
    printc(orange(str(UserEntryList)))
    print(" ")
    print("          UK AIRPORT: ",UserEntryList[0])
    print("          OVERSEAS AIRPORT: ",UserEntryList[1])
    print("          DISTANCE: ",UserEntryList[2],"KM")
    print("          FLIGHT COST PER SEAT",UserEntryList[8])
    print("          FLIGHT COST: ",UserEntryList[9])
    print(" ")
    print("          FLIGHT INCOME: ",UserEntryList[10])
    print("          FLIGHT PROFIT: ",round(UserEntryList[11],3))
    

########

#Q7 - Option 4: Clear data
def ClearData():
    global UKAPEntered
    global OVAPEntered
    global AirCft
    global FstSeats
    global StdSeats
    global AirCraftTypeEntered
    global NoFirstClassSeats
    global UserEntryList

    #ADD ALL VARIABLES AND ARRAYS

    print(" ")
    printc(red("You have chosen to Clear Data."))
    AirCraftTypeEntered = 0
    NoFirstClassSeats = 0
    UKAPEntered = 0
    OVAPEntered = 0
    FstSeats = 0
    StdSeats = 0
    UKAP = ""
    OVAP = ""
    AirCft = ""
    UserEntryList = [0*8]
    try:
        act.clear() #The clear() methof only empties the given list. It doesn't return any values.
        os.remove("myfile.txt") #To delete a file, you must import the OS module, and run its os.remove()
    except:
        print("...")

    print("Cleared all data. You can start over or exit using Option 5 in the main menu.")
    
##########

#2 - User's Menu
def user_menu():
    global User_Opt
    print(" ")
    print("--- ")
    print("MENU")
    print("1: Enter airport details")
    print("2: Enter flight details")
    print("3: Enter price plan and calculate profit")
    print("4: Clear data")
    print("5: Quit")
    print("--- ")
    print(" ")
    User_Opt = inputOption("Please enter your choice (1-5): ")
    
#3 - Asking the user's choice
def main():
    global User_Opt
    user_menu()
    if User_Opt == 0:
        print("You have chosen an invalid choice! The choice can't be zero. \nTry again!\n ")
        user_menu()
        User_Opt = inputOption("Please enter your choice (1-5): ")
    
    while User_Opt != 0:
    
        if User_Opt == 1:
            AirportDetails()

        elif User_Opt == 2:
            FlightDetails()

        elif User_Opt == 3:
            CalProfCheck()

        elif User_Opt == 4:
            ClearData()

        elif User_Opt == 5:
            print("You have chosen to quit \nBye!")
            break

        else:
            print("You have chosen an Invalid Option! \nTry again!")

        user_menu()

main()
    
print("Thank you for using this program!")
