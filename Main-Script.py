#Project 1: Bakterie-Dataanalyse


#imports
import numpy as np
import warnings
import matplotlib.pyplot as plt
import time

#Gustav ..
from dataLoad import *
#Nikolaj
from dataStatistics import *
#Benjamin
from dataPlot import *


#Vi var alle med til main-script


#Initial Statements:
quit = False   #loopet kører indtil quit = True
filter = False #flere ting i løbet af scriptet afhænger af hvorledes filteret er aktivt.
dataL = False  #Fortæller hvorledes om man har loadet data endnu
filterN = 2

bacteriaTypes = np.array(["salonella enterica","bascillus cereus",
                        "listeria","brochothrix thermosphacta"])


#Program loop:
while not quit:
    #Menu, hvor man kan se om filteret er aktivt. 
    print(" 1. Load data.\n",
           "2. Filter data.")
    if filter:
        print(" (Filter is active)")

    print(" 3. Display statistics.\n"
           " 4. Generate plots.\n",
           "5. Quit.\n",
           "Choose: ")
    nInput = input()
    
    #Sikkerhed for input:
    try:
        number = int(nInput)
    except ValueError:
        number = 0
    
    #Ekspertsystem:
    if number == 1:
        #dataLoad
        print("What is the filename: ")
        filename = input()

        #Sikkerhed for input:
        try:
            finalData = data = dataLoad(filename)
            print("Data is loaded.")
            dataL = True
            rows, col = np.shape(data)
            time.sleep(3)
        except FileNotFoundError:
            print("File not found!")
            time.sleep(1.5)

    elif (number == 2) and (dataL):
        #Filter
        print(' 1. Filter for Bacteria type.\n',
               '2. A range filter for Growth Rate.')
        if filter:
            print(' 3. Disable Filter')
           
        print('Choose: ')
        filterInput = input()
        #Sikkerhed for input:
        try:
            filterNumber = int(filterInput)
        except ValueError:
            filterNumber = 0

        
        if filterNumber == 1:
            print("Limiting data to one bacteria-type. Type which.\n",":")
            bacteriaInput = input() 

            bacNumb = np.arange(1,5)[bacteriaInput.lower() == bacteriaTypes]

            if (bacteriaInput.lower() == bacteriaTypes).any(): #sikkerhed for input
                finalData = data[data[:,2]==bacNumb]
                print("Data is filtered. ")
                filter = True
                filterN = 3
                time.sleep(1)
            else:
                print("Your input didn't match any bacteria.")
                time.sleep(1.5)
        
        
        elif (filterNumber == 2):
            #sikkerhed for input
            try: 
                print("The growth rate in the loaded data goes from {} to {}".format(np.min(data[:,1]),np.max((data[:,1]))))
                intervala=float(input("Filter growth rate from: "))
                intervalz=float(input("Filter growth rate to: "))
                
                if (intervala>intervalz):
                    print("Error. The from-value must be lower than the to-value!")
                elif (data[(data[:,1]>=intervala) & (data[:,1]<=intervalz)].size==0):
                    print("Interval returned an empty array. Filter initialization interrupted.")
                else:
                    finalData=data[(data[:,1]>=intervala) & (data[:,1]<=intervalz)]
                    filter = True
                    filterN = 3
                    print("Data is filtered.")
            except ValueError:
                print("Error. Input must be a number, where the decimals are seperated by a period.")
            finally:
                time.sleep(1)
        elif (filterNumber == 3) and (filter):
            finalData = data
            filter = False
            filterN = 2
            print("Filter is removed.")
            time.sleep(1)
        else:
            print("Wrong input. You must type a number between 1 and {}!".format(round(filterN)))
            time.sleep(1.5)


    elif (number == 3) and (dataL):
        #Display Statistics
        print("What statistic do you want: ")
        statistic = input()
        #Sikkerhed for input
        try:
            output = dataStatistics(finalData, statistic)
            print(statistic[0].upper()+statistic[1:].lower(),":",output)
            time.sleep(1.5)
        except NameError:
            print("You have not loaded any data yet!")
            time.sleep(1)
        except IndexError:
            print("You must type something!")
            time.sleep(1)

    elif (number == 4) and (dataL):
        #Generate plots
        try:
            dataPlot(finalData)
        except NameError:
            print("You have not loaded any data yet!")
            time.sleep(1)


    elif number == 5:
        #Quit
        print("Goodbye.")
        quit = True
    elif (not dataL) and (number<=5) and (number>=1):
        print("Error. You have not loaded any data!")
        time.sleep(1)
    else:
        print("Error. Your input wasn't a whole number between 1 and 5!")
        time.sleep(1)
