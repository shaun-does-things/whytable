import datetime
import math
import random
import json

# assume camelCase

#declared var/const/list
day = datetime.datetime.now()
formattedDay = day.strftime("%y/%m/%d")
formattedTime = day.strftime("%H:%M")
todayNum = int(day.strftime("%w"))-1
todayWord = day.strftime("%a")
filePath = "timetable.json"
loadedFile = open(filePath,"r")
table = json.load(loadedFile)

# menu
def menu():
    print("Welcome!\nThe day is",formattedDay,"\nAnd the time is",formattedTime)
    print("Select an option!\n[1]: View today's timetable\n[2]: View timetable for a different day\n[3]: Enter edit mode\n[0]: Exit")
    selection = int(input("Choice: ")) 
    match selection:
        case 1:
            print("Today's tasks are:")
            print(table[todayNum][1:])
            blank = input("enter to continue")
            menu()
        case 2:
            print("Select a day! (Format is abreviated, so Mon/Tue/Wed etc..)")
            dayChoice = input("Choice: ")
            for i in range(0,7):
                if dayChoice == table[i][0]:
                    print(table[i][1:])
                    blank = input("enter to continue")
                    menu()
                else:
                    print("error, day not found")
                    menu()
        case 3:
            print("You're in edit mode!\n[1]: Add element\n[2]: Remove element\n[3]: Write to file.")
            editChoice = int(input("Choice: "))

menu()