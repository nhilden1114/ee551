'''
Calculator to determine what day of the week you were born using Tkinter
Created by Nicole Hilden
May 2020
Final Project for EE551
I pledge my honor that I have abided by the Stevens Honor System
'''
import datetime
import tkinter
from tkinter import *

#Initializes the GUI
gui = Tk()

#Set the background color and title of the GUI
gui.configure(background="light blue")
gui.title("What day of the week were you born?")

#Configuration of the GUI window
gui.geometry("370x400")

#Creates the text label that is present within the GUI window at all times
program_label = Label(gui, text="Please select the year, month, and date of your birth")

#Grid is used throughout the program
#Determines the placement of all of the widgets in a row, column structure
program_label.grid(columnspan=4, ipadx=15)

#Initializing variables that will be used globally
user_choice = Label(gui) #month the user chooses
date_scale = Scale(gui) #scale for picking date
output = Label(gui) #output containing declaration of what day of the week you were born
button_calc = Button(gui) #Calculate button
yearVal = 2020 #initializing year to current year, will be updated by dropdown
monthVal = 1 #initializing month to 1, will be updated by month buttons
bmonth = "" #birth month chosen by the user
clicked = StringVar() #create an instance of the variable class StringVar()
clicked.set("2020") #initialize to 2020

#Options for the dropdown that contain the past 100 years
options = ["2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007", "2006", "2005",
            "2004", "2003", "2002", "2001", "2000", "1999", "1998", "1997", "1996", "1995", "1994", "1993", "1992", "1991", "1990",
            "1989", "1988", "1987", "1986", "1985", "1984", "1983", "1982", "1981", "1980", "1979", "1978", "1977", "1976", "1975",
            "1974", "1973", "1972", "1971", "1970", "1969", "1968", "1967", "1966", "1965", "1964", "1963", "1962", "1961", "1960", 
            "1959", "1958", "1957", "1956", "1955", "1954", "1953", "1952", "1951", "1950", "1949", "1948", "1947", "1946", "1945", 
            "1944", "1943", "1942", "1941", "1940", "1939", "1938", "1937", "1936", "1935", "1934", "1933", "1932", "1931", "1930",
            "1929", "1928", "1927", "1926", "1925", "1924", "1923", "1922", "1921", "1920"]

#Dropdown where the user will choose their birth year
#After choosing a year, updateMonth is called to clear out old selection and prompt the user to choose a month
def chooseYear():

    #Create dropdown widget
    drop = OptionMenu(gui, clicked, *options,  command=updateMonth)
    drop.grid(row=2, column=0, padx=10, pady=10)

#Clears previously selected info and prompts the user to re-select a month
def updateMonth(self):
    user_choice.config(text="Please choose a month")
    output.grid_forget()
    button_calc.grid_forget()

#Clears previous output
def clearCalc(self):
    output.grid_forget()

#Detemine what month the user has selected
def month(num):

    #Clear old output
    output.grid_forget()

    #Array of months
    months = ["January", "February", "March", "April", "May", "June", "July", "August",
             "September", "October", "November", "December"]
    
    #Determine what month the user has selected
    bmonth = months[num-1]
    
    #Placement and configuarion of the user's chosen month displayed as a label in the GUI
    user_choice.grid(row=7, columnspan=3, padx=10, pady=10)
    user_choice.config(text="You have chosen " + bmonth)

    #Updates the global variable monthVal to the value of the user's chosen month
    global monthVal
    monthVal = num

    #Creates the date slider
    chooseDay(monthVal)

    return monthVal

#Determines if a given year is a leap year
def leapYear(yearVal):

    #Get the most current value from the dropdown
    yearVal = int(clicked.get())
    
    if (yearVal % 4) == 0:
        if (yearVal % 100) == 0:
            if (yearVal % 400) == 0:
                return True 
            else:
                return False
        else:
            return True
    else:
        return False

#Creates the date slider in the GUI for the user to select which day of the month they were born
#Scales all call clearCalc so that user no longer sees previous calculation
def chooseDay(month):
    
    #if month is April, June, September, or November it will have 30 days
    if (month == 4 or month == 6 or month == 9 or month == 11):
        
        #Configure the scale from 1-30
        date_scale.config(from_=1, to=30, orient=HORIZONTAL, command=clearCalc) 
        date_scale.grid(row=8, columnspan=3, pady=5)

    #If month is February
    elif month == 2:
        
        #If the year chosen is a leap year
        if leapYear(yearVal):

            #Configure the scale from 1-29
            date_scale.config(from_=1, to=29, orient=HORIZONTAL, command=clearCalc)
            date_scale.grid(row=8, columnspan=3, pady=5)
        
        #If the year chosen is not a leap year
        else:

            #Configure the scale from 1-28
            date_scale.config(from_=1, to=28, orient=HORIZONTAL, command=clearCalc)
            date_scale.grid(row=8, columnspan=3, pady=5)
    
    #If month is January, March, May, July, August, October, or December
    elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        
        #Configure the scale from 1-31
        date_scale.config(from_=1, to=31, orient=HORIZONTAL, command=clearCalc) 
        date_scale.grid(row=8, columnspan=3, pady=5)

    #Call the function to create the Calculate button
    computeDOW()
    
    return

#Creates all of the buttons for each of the 12 months
def createButtons():

    #All buttons have their respective text labels and are placed in a 3x4 grid
    #When clicked, the command calls on the month(num) function to collect their selection

    button_jan = Button(gui, text="January", height=2, width=8, command=lambda: month(1))
    button_jan.grid(row=3, column=0)

    button_feb = Button(gui, text="February", height=2, width=8, command=lambda: month(2))
    button_feb.grid(row=3, column=1)

    button_mar = Button(gui, text="March", height=2, width=8, command=lambda: month(3))
    button_mar.grid(row=3, column=2)

    button_apr = Button(gui, text="April", height=2, width=8, command=lambda: month(4))
    button_apr.grid(row=4, column=0)

    button_may = Button(gui, text="May", height=2, width=8, command=lambda: month(5))
    button_may.grid(row=4, column=1)

    button_jun = Button(gui, text="June", height=2, width=8, command=lambda: month(6))
    button_jun.grid(row=4, column=2)

    button_jul = Button(gui, text="July", height=2, width=8, command=lambda: month(7))
    button_jul.grid(row=5, column=0)

    button_aug = Button(gui, text="August", height=2, width=8, command=lambda: month(8))
    button_aug.grid(row=5, column=1)

    button_sep = Button(gui, text="September", height=2, width=8, command=lambda: month(9))
    button_sep.grid(row=5, column=2)

    button_oct = Button(gui, text="October", height=2, width=8, command=lambda: month(10))
    button_oct.grid(row=6, column=0)

    button_nov = Button(gui, text="November", height=2, width=8, command=lambda: month(11))
    button_nov.grid(row=6, column=1)

    button_dec = Button(gui, text="December", height=2, width=8, command=lambda: month(12))
    button_dec.grid(row=6, column=2)

#Configures the Calculate button 
def computeDOW():

    #When clicked, compute is called to create the output for the user
    button_calc.config(text="Calculate", height=2, width=8, command=compute)
    button_calc.grid(row=9, columnspan=3, pady=10)

#Computes the day of the week given a month, day, and year
def compute():

    #Datetime library determines the weekday of a given date using values of 0-6 where 0 is Monday and 6 is Sunday
    day_val = datetime.datetime(int(clicked.get()), monthVal, int(date_scale.get())).weekday()
    
    #Array of all of the days of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    #Uses day_val as an index to get string value of weekday
    outputStr = days_of_week[day_val]

    #Placement and configuration of output for the user
    output.config(text="You were born on a " + outputStr)
    output.grid(row=10, columnspan=3, ipadx=15)


if __name__ == "__main__":
    
    #Calls on the functions that create the year dropdown and month buttons
    chooseYear()
    createButtons()

    #Start the GUI
    gui.mainloop()