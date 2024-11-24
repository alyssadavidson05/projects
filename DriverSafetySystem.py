import math
import random
from tkinter import *
import tkinter as tk

#variables- Alyssa Initaialized the variables
user_weight = random.randint(0, 250)
user_height = random.randint(0, 10)
max_heart_rate = 0
low_heart_rate = 0
high_heart_rate = 0
user_heart_rate = random.randint(0, 185)
pressure_sensored = random.randint(0,20)
vehicle_shift = random.randint(0, 5)
seat_position = 0
wheel_position = 0

# James -- created the GUI
#customtkinter.set_default_color_theme("blue")
window = Tk()
window.title("GUI Test") #set gui title

gendervar = " "
heightvar = " "
randomvar  = 0 # spare variable if we want to use it

# pseudorandom value generators ------------------------------------------
#   for blood pressure
f1 = random.randrange(90, 131) 
f2 = random.randrange(60, 91)
bpvar = f"{f1}/{f2} mm Hg"

# for heartrate
hr = random.randrange(85, 191)


# for weight
weight = random.randrange(110, 210)

# ------------------------------------------------------------------------

lbl = Label(window, text="User data gathered:", font=("Arial Bold", 30), pady=35) #add label window
lbl.grid(column=0, row=0)

window.geometry('1280x720') #set default window size

lbl2 = Label(window, text="Blood Pressure:", font=("Arial Bold", 16)) #add label window
lbl2.grid(column=0, row=1)
lbl2response = Label(window, text=bpvar, font=("Arial Bold", 16), padx=20)
lbl2response.grid(column=1, row=1)

lbl3 = Label(window, text="Heartrate:", font=("Arial Bold", 16)) #add label window
lbl3.grid(column=0, row=2)
lbl3response = Label(window, text=hr, font=("Arial Bold", 16), padx=20)
lbl3response.grid(column=1, row=2)

lbl4 = Label(window, text="Weight:", font=("Arial Bold", 16)) #add label window
lbl4.grid(column=0, row=3)
lbl4response = Label(window, text=weight, font=("Arial Bold", 16), padx=20)
lbl4response.grid(column=1, row=3)

lbl5 = Label(window, text="Gender:", font=("Arial Bold", 16)) #add label window
lbl5.grid(column=0, row=4)
lbl5response = Label(window, text="#", font=("Arial Bold", 16), padx=20)
lbl5response.grid(column=1, row=4)

lbl6 = Label(window, text="Height:", font=("Arial Bold", 16)) #add label window
lbl6.grid(column=0, row=5)
lbl6response = Label(window, text="#", font=("Arial Bold", 16), padx=20)
lbl6response.grid(column=1, row=5)


lbl7 = Label(window, text="Age:", font=("Arial Bold", 16)) #add label window
lbl7.grid(column=0, row=6)
lbl7response = Label(window, text="#", font=("Arial Bold", 16), padx=20)
lbl7response.grid(column=1, row=6)

lbl8 = Label(window, text="", font=("Arial Bold", 16)) #add label window
lbl8.grid(column=0, row=7)

lblEntry1 = Label(window, text="Please Enter Gender:", font=("Arial Bold", 16))
lblEntry1.grid(column=3, row=1)
lblEntry2 = Label(window, text="Please Enter Height:", font=("Arial Bold", 16))
lblEntry2.grid(column=3, row=2)
lblEntry3 = Label(window, text="Please Enter Age:", font=("Arial Bold", 16))
lblEntry3.grid(column=3, row=3)

entry1 = Entry(window, width=15)
entry1.grid(column=4, row=1)
entry2 = Entry(window, width=15)
entry2.grid(column=4, row=2)
entry3 = Entry(window, width=15)
entry3.grid(column=4, row=3)

answerEntrylbl = Label(window, text="Please Enter Yes or No:", font=("Arial Bold", 16))
answerEntrylbl.grid(column=3, row=4)
answerEntry = Entry(window, width=15)
answerEntry.grid(column=4, row=4)

# James
def entered():
    gendervar = entry1.get()
    heightvar = entry2.get()
    randomvar = entry3.get()
    lbl5response.configure(text=gendervar)
    lbl6response.configure(text=heightvar)
    lbl7response.configure(text=randomvar)
    automatic_aujustment_function()

# Alyssa
def answer_function():

    global user_answer
    #gets the answer inputted by the user
    user_answer = answerEntry.get()
    return user_answer

# Berek -- created the automatic adjustment system
def automatic_aujustment_function():
    if (user_height == 5):
        seat_position == 5
    if (user_height == 4):
        seat_position == 4
    if (user_height == 3):
        seat_position == 3
    if (user_height == 2):
        seat_position == 2
    if (user_height == 1):
        seat_position == 1
    
    global lbl8
    lbl8 = Label(window, text="Are you comfortable with the seat position?", font=("Arial Bold", 16))
    lbl8.grid(column=0, row=7)

def automatic_aujustment_function2():

    answer_function()

    if ((user_answer == "No") or (user_answer == "no")):
        lbl8.configure(text="Click 'DONE' when you are done adjusting the seat")
        donebtn = Button(window, text="Done", bg="blue", fg="white", command=automatic_aujustment_function3)
        donebtn.grid(column=2, row=5)
    elif ((user_answer == "yes") or (user_answer == "yes")):
        lbl8.configure(text="You are ready to drive.")
        if ((safe_heart_rate_function() != 0) and warning_system_function() == 0):
            lbl8.configure(text="Are you okay?")
            answerbtn.configure(command=emergency_stop_system_function)
        elif(safe_heart_rate_function() != 0):
            lbl8.configure(text="Are you okay?")
            answerbtn.configure(command=emergency_stop_system_function2)
        else:
            lbl8.configure(text="Your heart rate is good.")

def automatic_aujustment_function3():
    lbl8.configure(text="Adjusting steering wheel now.")
    if ((safe_heart_rate_function() != 0) and warning_system_function() == 0):
        lbl8.configure(text="Are you okay?")
        answerbtn.configure(command=emergency_stop_system_function)
    elif(safe_heart_rate_function() != 0):
        lbl8.configure(text="Are you okay?")
        answerbtn.configure(command=emergency_stop_system_function2)
    else:
        lbl8.configure(text="Your heart rate is good.")

# konner -- created the warning system
def warning_system_function():
    #if the car is in park
    if (vehicle_shift == 0):
        print("Be sure to keep hands on the wheel when driving.")
        return 1
    #If the car is in froward
    elif (vehicle_shift % 2 == 0):
        #Their hands aren't on the wheel
        if (pressure_sensored % 5 == 0):
            print("Please put both hands on the wheel.")
            return 0
        #One hand is on the wheel
        elif (pressure_sensored % 2 != 0):
            print("Please place your other hand back on the wheel.")
            return 1
        #both hands are on the wheel
        elif (pressure_sensored % 2 == 0):
            return 1
    #if the car is in reverse
    elif (vehicle_shift % 2 != 0):
        #If there is a hand on the wheel
        if (pressure_sensored % 5 != 0):
            return 1
         #If there are no hands on the wheel
        elif (pressure_sensored % 5 == 0):
            print("Please put one or both hands on the wheel.")
            return 0
        
# Alyssa and Claudia created safe_heart_rate_ function and all emergencey stop functions
def safe_heart_rate_function():
    #calculates the average heart rate and the low and high
    user_age = randomvar
    user_age = int(user_age)
    max_heart_rate = 220 - user_age
    low_heart_rate = max_heart_rate * .64
    high_heart_rate = max_heart_rate * .76

    #normal heart rate
    if (low_heart_rate <= user_heart_rate <= high_heart_rate):
        return 0
    #low heart rate
    elif (user_heart_rate < low_heart_rate):
        return -1
    #high heart rate
    elif (user_heart_rate > high_heart_rate):
        return 1

#Emergency Stop System
def emergency_stop_system_function():
    #If the drivers hands aren't on the wheel and their heart rate is adnormal this will run.
    
    #gets the answer the driver inputted
    answer_function()
    
    #asks if driver is okay

    #driver answers yes and continues driving like normal
    if ((user_answer == "yes") or (user_answer == "Yes")):
        lbl8.configure(text="That's good to hear.")
        return 1
    #driver answers no and authorties are contacted
    elif ((user_answer == "No") or (user_answer == "no")):
        lbl8.configure(text="We are contacting emergency services and an emergency contact. The vehicle will now pull over.")
        return 1

def emergency_stop_system_function2():
    #If the drivers heart rate gets to an adnormal rate this will run.

        #gets answer the driver inptted
        answer_function()

        #asks driver if they are okay

        #driver says yes and continues driving like normal
        if ((user_answer == "yes") or (user_answer == "Yes")):
            lbl8.configure(text="That's good to hear.")
            return 1
        #driver says no and asks if they need to contact anyone
        elif ((user_answer == "No") or (user_answer == "no")):
            lbl8.configure(text="Would you like to contact someone?")
            answerbtn.configure(command=emergency_stop_system_function3)

def emergency_stop_system_function3():

    #gets answer inputted from driver
    answer_function()

    #asks if they would like to contact anyone

    #says yes and asks who to contact
    if ((user_answer == "yes") or (user_answer == "Yes")):
        lbl8.configure(text="Who would you like to contact?")

        #creates lable for prompt in GUI
        contactlbl = Label(window, text="Please Enter Contact", font=("Arial Bold", 16))
        contactlbl.grid(column=3, row=7)
        #creates entry in GUI for input
        global contactEntry
        contactEntry = Entry(window, width=15)
        contactEntry.grid(column=4, row=7)
        #creates button in GUI to contact person
        contactbtn = Button(window, text="Contact", bg="blue", fg="white", command=contact_function)
        contactbtn.grid(column=4, row=8)
        return 1
    #driver answered no so asks if they need to stop
    elif((user_answer == "No") or (user_answer == "no")):
        lbl8.configure(text="Would you like to preform an emergency stop?")
        answerbtn.configure(command=emergency_stop_system_function4)

def emergency_stop_system_function4():

    #gets drivers answer to question
    answer_function()
    
    #asks if they need to stop

    #answer is yes so the car is pulled over
    if ((user_answer == "yes") or (user_answer == "Yes")):
        lbl8.configure(text="Performing an emergency stop.")
        return 1
    #answer is no so the car continues driving like normal
    elif ((user_answer == "No") or (user_answer == "no")):
        lbl8.configure(text="Okay, drive safe.")
        return 1

# Alyssa
def contact_function():
    #gets contact inputted by driver and contacts them
    lbl8.configure(text="Contacting: " + str(contactEntry.get()))

#James
submitbtn = Button(window, text="Submit", bg="blue", fg="white", command=entered) # bg is the button background color while fg is the font color
submitbtn.grid(column=4, row=5)

#Alyssa
answerbtn = Button(window, text="Answered", bg="blue", fg="white", command=automatic_aujustment_function2)
answerbtn.grid(column=4, row=6)


entry1.focus()

window.mainloop()
