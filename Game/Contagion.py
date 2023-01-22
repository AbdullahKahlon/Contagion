#Import Modules
from tkinter import *
from time import sleep
import threading
import datetime
import math
import random


#declare variables, we will be making all variables global in all functions to take advantage of tkinters functionality, as well as to avoid having to pass in and return values every tick
global win, infections, infectivity, count, currentdate, points, upgrade_cost_a, upgrade_cost_b, upgrade_cost_c, upgrade_cost_d, upgrade_cost_e, upgrade_cost_f, upgrade_cost_g, upgrade_cost_h, infectivity_upgrades, symptom_upgrades, misc_upgrades, lethality, mutation, population, cure, dayspassed, deadpop, tickspeed, alivepop, livingpop, infc_per_pnt

win = 0

mutation = 0.001 #mutation chance
lethality = 0.001 #lethality, controls how fast people die
misc_upgrades = {"cure": 0, "mutation": 0, "tick speed": 0} #dictionary to keep track of miscellaneous upgrades
symptom_upgrades = {"nausea": 0, "cough": 0, "fever": 0} #dictionary to keep track of lethality upgrades
infectivity_upgrades = {"air": 0, "land": 0, "water": 0} #dictionary to keep track of infectivity upgrades

#starting upgrade costs
upgrade_cost_a = 4 
upgrade_cost_b = 16
upgrade_cost_c = 64
upgrade_cost_d = 3
upgrade_cost_e = 9
upgrade_cost_f = 27
upgrade_cost_g = 1000
upgrade_cost_h = 1000

infections = 1 #infections start at 1, as it takes about 2 ticks for the window to load in so it shows 3 infection when the player starts
tickspeed = 1 #starting tick speed
infectivity = 1 #infections per second
points = 4 #starting upgrade points
infc_per_pnt = 25 #infections needed to earn a point
count = 0 #no idea what this is for, if i remove it everything breaks, :)
currentdate = '' #initialize date value
population = 8011626402 #world population
cure = 0 #cure percentage
dayspassed = 0 #variable used to count days since game started
deadpop = 0 #used to keep track of deaths
livingpop = 0 #used to keep track of population alive



def tick():
    global win, infections, infectivity, count, currentdate, points, upgrade_cost_a, upgrade_cost_b, upgrade_cost_c, upgrade_cost_d, upgrade_cost_e, upgrade_cost_f, upgrade_cost_g, upgrade_cost_h, infectivity_upgrades, symptom_upgrades, misc_upgrades, lethality, mutation, population, cure, dayspassed, deadpop, tickspeed, infc_per_pnt

    
    deadpop += infections*lethality
    print(infections*lethality)
    if (infections + (infectivity - (infections*lethality))) > (population - deadpop):
        infectivity = 0
    infections += infectivity - (infections*lethality)
    population -= deadpop


    uninfecpop = population-infections

    if uninfecpop-infectivity <= 0:
        infectivity = 0
        infections = population
        unfecpop.configure(text=("Population Uninfected: 0"))
    
    else:
        unfecpop.configure(text=("Population Uninfected: " + str(math.floor(uninfecpop))))

    if population-lethality <= 0:
        win = 2
        population = 0
        infections = 0
        lethality = 0
        alivepop.config(text=("Population Alive: 0"))
        infc.configure(text=("Infections: 0"))
    else:   
        alivepop.config(text=("Population Alive: " + str(math.floor(population-deadpop))))

    

    dayspassed += 1
    
    if dayspassed > 0:
        cure += round(random.uniform(-0.33, 1.66), 3)
    if cure < 0:
        cure = 0.01
    cure_prog.configure(text=("Cure Progress: " + str(round(cure,3)) + "%"))

    if cure >= 100:
        win = 1

    


    
    
    infc.configure(text=("Infections: " + str(math.floor(infections))))
    points += ((1/infc_per_pnt)*infectivity)+(cure*1.07)+((infections+lethality)/50) 
    pnts.configure(text=("Points: " + str(math.floor(points))))
    
    
    
    
    drate.config(text=("Deaths per day: " + str(round(infections*lethality,3))))

    count+=1
    currentdate = datetime.date.today() + datetime.timedelta(days=count)
    datelbl.configure(text=("Date: " + str(currentdate)))
    
    lethalitylbl.config(text =("Lethality: " + str(round(lethality,3)) + "%"))    
    irate.configure(text=("Infections per day: " + str(round(infectivity,2))))

    misc1.config(text="Cure Resistance " + str(misc_upgrades["cure"]+1) + "\nCost: " +str(upgrade_cost_g))
    misc3.config(text="Tick Speed " +str(misc_upgrades["tick speed"]+1) +"\nCost: " +str(upgrade_cost_h))

    
    
    

    if win == 0:
        sleep(tickspeed)
        t = threading.Timer(tickspeed, tick)
        t.start()
    elif win == 1:
        for widget in window.winfo_children():
            widget.destroy()
        gameover=Label(window, text=("Game Over"), fg='yellow', bg='black', font=("Fixedsys Excelsior 3.01", 70))
        reason=Label(window, text=("A vaccine was successfully developed for your disease. Try again."), fg='blue', bg='black', font=("Fixedsys Excelsior 3.01", 15))
        gameover.place(x=310, y=100)
        reason.place(x=230, y=215)
        creditslbl=Label(window, text=("Credits" + "\nGame developed by Abdullah Shahid and Nathan Yoon" + "\n Art? What art" + "\n Music taken off google dont sue pls" + "\n Shout out Tai Poole for showing us the light" + "\nbig thank you to COVID-19 and Plague Inc they did it first"), fg='#333333', bg='black', font=("Fixedsys Excelsior 3.01", 15))
        creditslbl.place(x=220, y=400)
        print("lose")
    else:
        sleep(2)
        for widget in window.winfo_children():
            widget.destroy()
        gameover=Label(window, text=("Game Over"), fg='yellow', bg='black', font=("Fixedsys Excelsior 3.01", 70))
        daystaken=Label(window, text=("You eradicated the human race in " + str(dayspassed) + " days."), fg='red', bg='black', font=("Fixedsys Excelsior 3.01", 15))
        gameover.place(x=310, y=100)
        daystaken.place(x=305, y=215)
        creditslbl=Label(window, text=("Credits" + "\nGame developed by Abdullah Shahid and Nathan Yoon" + "\n Art? What art" + "\n Shout out Tai Poole for showing us the light" + "\nbig thank you to COVID-19 and Plague Inc they did it first"), fg='#333333', bg='black', font=("Fixedsys Excelsior 3.01", 15))
        creditslbl.place(x=220, y=400)
        print("win")

def add():
    global uninfecpop, infections, infectivity, count, currentdate, points, upgrade_cost_a, upgrade_cost_b, upgrade_cost_c, upgrade_cost_d, upgrade_cost_e, upgrade_cost_f, upgrade_cost_g, upgrade_cost_h, infectivity_upgrades, symptom_upgrades, misc_upgrades, lethality, mutation, population, cure, dayspassed, deadpop, tickspeed, infc_per_pnt
    print("a")
    uninfecpop = population-infections
    if not (infections + infectivity > (population-deadpop)):
        infections += 1*infectivity
        points += (1/infc_per_pnt)*infectivity+(0.1*cure)
        pnts.configure(text=("Points: " + str(math.floor(points))))
        infc.configure(text=("Infections: " + str(math.floor(infections))))

    if uninfecpop-infectivity <= 0:
        infectivity = 0
        infections = population
        unfecpop.configure(text=("Population Uninfected: 0"))
    
def air_upgrade():
    global infections, infectivity, count, currentdate, points, upgrade_cost_a, upgrade_cost_b, upgrade_cost_c, upgrade_cost_d, upgrade_cost_e, upgrade_cost_f, upgrade_cost_g, upgrade_cost_h, infectivity_upgrades, symptom_upgrades, misc_upgrades, lethality, mutation, population, cure, dayspassed, deadpop, tickspeed, infc_per_pnt

    if points >= upgrade_cost_a:
        infectivity_upgrades["air"] += 1
        points -= upgrade_cost_a
        infectivity *= 4.5
        upgrade_cost_a *=64
        infc_per_pnt += 25
    
    
    pnts.configure(text=("Points: " + str(math.floor(points))))
    
    print(infectivity_upgrades["air"])
    if infectivity_upgrades["air"] == 4:
        infec1.configure(text="Air Transmission \nMaxed", command = '')
    else:
        infec1.configure(text="Air Transmission " + str(infectivity_upgrades["air"]+1) + "\nCost: " + str(upgrade_cost_a))

def land_upgrade():
    global infections, infectivity, count, currentdate, points, upgrade_cost_a, upgrade_cost_b, upgrade_cost_c, upgrade_cost_d, upgrade_cost_e, upgrade_cost_f, upgrade_cost_g, upgrade_cost_h, infectivity_upgrades, symptom_upgrades, misc_upgrades, lethality, mutation, population, cure, dayspassed, deadpop, tickspeed, infc_per_pnt

    if points >= upgrade_cost_b:
        infectivity_upgrades["land"] += 1
        points -= upgrade_cost_b
        infectivity *= 4.5
        upgrade_cost_b *=64
        infc_per_pnt += 25
    pnts.configure(text=("Points: " + str(math.floor(points))))
    print(infectivity_upgrades["land"])
    if infectivity_upgrades["land"] == 4:
        infec2.configure(text="Land Transmission \nMaxed", command = '')
    else:
        infec2.configure(text="Land Transmission " + str(infectivity_upgrades["land"]+1) + "\nCost: " + str(upgrade_cost_b))

def water_upgrade():
    global infections, infectivity, count, currentdate, points, upgrade_cost_a, upgrade_cost_b, upgrade_cost_c, upgrade_cost_d, upgrade_cost_e, upgrade_cost_f, upgrade_cost_g, upgrade_cost_h, infectivity_upgrades, symptom_upgrades, misc_upgrades, lethality, mutation, population, cure, dayspassed, deadpop, tickspeed, infc_per_pnt

    if points >= upgrade_cost_c:
        infectivity_upgrades["water"] += 1
        points -= upgrade_cost_c
        infectivity *= 4.5
        upgrade_cost_c *= 64
        infc_per_pnt += 25
    pnts.configure(text=("Points: " + str(math.floor(points))))
    print(infectivity_upgrades["water"])
    if infectivity_upgrades["water"] == 4:
        infec3.configure(text="Water Transmission \nMaxed", command = '')
    else:
        infec3.configure(text="Water Transmission " + str(infectivity_upgrades["water"]+1) + "\nCost: " + str(upgrade_cost_c))

def fever_upgrade():
    global infections, infectivity, count, currentdate, points, upgrade_cost_a, upgrade_cost_b, upgrade_cost_c, upgrade_cost_d, upgrade_cost_e, upgrade_cost_f, upgrade_cost_g, upgrade_cost_h, infectivity_upgrades, symptom_upgrades, misc_upgrades, lethality, mutation, population, cure, dayspassed, deadpop, tickspeed, alivepop, infc_per_pnt

    if points >= upgrade_cost_d:
        symptom_upgrades["fever"] += 1
        points -= upgrade_cost_d
        lethality *= 1.5
        upgrade_cost_d *= 27
    pnts.configure(text=("Points: " + str(math.floor(points))))
    print(symptom_upgrades["fever"])
    if symptom_upgrades["fever"] == 4:
        lethal1.configure(text="Fever \nMaxed", command = '')
    else:
        lethal1.configure(text="Fever " + str(symptom_upgrades["fever"]+1) + "\nCost: " + str(upgrade_cost_d))

def nausea_upgrade():
    global infections, infectivity, count, currentdate, points, upgrade_cost_a, upgrade_cost_b, upgrade_cost_c, upgrade_cost_d, upgrade_cost_e, upgrade_cost_f, upgrade_cost_g, upgrade_cost_h, infectivity_upgrades, symptom_upgrades, misc_upgrades, lethality, mutation, population, cure, dayspassed, deadpop, tickspeed

    if points >= upgrade_cost_f:
        symptom_upgrades["nausea"] += 1
        points -= upgrade_cost_f
        lethality *= 1.5
        upgrade_cost_f *= 27
    pnts.configure(text=("Points: " + str(math.floor(points))))
    print(symptom_upgrades["nausea"])
    if symptom_upgrades["nausea"] == 4:
        lethal3.configure(text="Nausea \nMaxed", command = '')
    else:
        lethal3.configure(text="Nausea " + str(symptom_upgrades["nausea"]+1) + "\nCost: " + str(upgrade_cost_f))

def cough_upgrade():
    global infections, infectivity, count, currentdate, points, upgrade_cost_a, upgrade_cost_b, upgrade_cost_c, upgrade_cost_d, upgrade_cost_e, upgrade_cost_f, upgrade_cost_g, upgrade_cost_h, infectivity_upgrades, symptom_upgrades, misc_upgrades, lethality, mutation, population, cure, dayspassed, deadpop, tickspeed

    if points >= upgrade_cost_e:
        symptom_upgrades["cough"] += 1
        points -= upgrade_cost_e
        lethality *= 1.5
        upgrade_cost_e *= 27
    pnts.configure(text=("Points: " + str(math.floor(points))))
    print(symptom_upgrades["cough"])
    if symptom_upgrades["cough"] == 4:
        lethal2.configure(text="Cough \nMaxed", command = '')
    else:
        lethal2.configure(text="Cough " + str(symptom_upgrades["cough"]+1) + "\nCost: " + str(upgrade_cost_e))
    
        
def cure_upgrade():
    global infections, infectivity, count, currentdate, points, upgrade_cost_a, upgrade_cost_b, upgrade_cost_c, upgrade_cost_d, upgrade_cost_e, upgrade_cost_f, upgrade_cost_g, upgrade_cost_h, infectivity_upgrades, symptom_upgrades, misc_upgrades, lethality, mutation, population, cure, dayspassed, deadpop, tickspeed


    if points >= upgrade_cost_g:
        misc_upgrades["cure"] += 1
        points -= upgrade_cost_g
        cure -= 10
        upgrade_cost_g *=10
    pnts.configure(text=("Points: " + str(math.floor(points))))

def tick_upgrade():
    global infections, infectivity, count, currentdate, points, upgrade_cost_a, upgrade_cost_b, upgrade_cost_c, upgrade_cost_d, upgrade_cost_e, upgrade_cost_f, upgrade_cost_g, upgrade_cost_h, infectivity_upgrades, symptom_upgrades, misc_upgrades, lethality, mutation, population, cure, dayspassed, deadpop, tickspeed

    if points >= upgrade_cost_h:
        misc_upgrades["tick speed"] += 1
        points -= upgrade_cost_h
        tickspeed -= 0.1
        upgrade_cost_h *=10
    pnts.configure(text=("Points: " + str(math.floor(points))))
    
 



t = threading.Timer(tickspeed, tick)
t.start() 


# Create object 
window = Tk()

      
# Adjust details 
window.geometry("1024x576")
window.configure(bg='black')
window.title('Contagion')
window.iconbitmap("contagionicon.ico")
window.resizable(width=False, height=False)


#widgets
infc=Label(window, text=("Infections: " + str(math.floor(infections))), fg='white', bg='black', font=("Fixedsys Excelsior 3.01", 30))
infc.place(x=10, y=10)

cornerlogo = PhotoImage(file='cornerlogo.png')
logo = Label(window, image = cornerlogo, highlightthickness = 0, bd = 0)
logo.place(x=670, y=0)

bottomline = PhotoImage(file='bottomline.png')
bline = Label(window, image = bottomline, highlightthickness = 0, bd = 0)
bline.place(x=0, y=135)

tline = Label(window, image = bottomline, highlightthickness = 0, bd = 0)
tline.place(x=0, y=495)

alivepop=Label(window, text=("Population Alive: " + str(population)), fg='green', bg='black', font=("Fixedsys Excelsior 3.01", 12))
alivepop.place(x=750, y=55)

unfecpop=Label(window, text=("Population Uninfected: " + str(population - infections )), fg='green', bg='black', font=("Fixedsys Excelsior 3.01", 12))
unfecpop.place(x=750, y=80)

lethalitylbl = Label(window, text =("Lethality: 0%"), fg="red", bg = 'black', font=("Fixedsys Excelsior 3.01", 20))
lethalitylbl.place(x=375, y=518)

datelbl=Label(window, text=("Date: " + str(currentdate)), fg='green', bg='black', font=("Fixedsys Excelsior 3.01", 12))
datelbl.place(x=750, y=105)

irate=Label(window, text=("Infections per day: " + str(math.floor(infectivity))), fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))
irate.place(x=12, y=55)

drate=Label(window, text=("Deaths per day: " + str(lethality)), fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))
drate.place(x=12, y=75)

cure_prog = Label(window, text =("Cure Progress: 0%"), fg="blue", bg = 'black', font=("Fixedsys Excelsior 3.01", 20))
cure_prog.place(x=25, y=518)



pnts = Label(window, text =("Points: " + str(points)), fg="brown", bg = 'black', font=("Fixedsys Excelsior 3.01", 14))
pnts.place(x=13, y=95)

clicker_label = Label(window, text =("Infect"), fg="red", bg = 'black', font=("Fixedsys Excelsior 3.01", 14))
clicker_label.place(x=956, y=468)

#buttons
infectbtn= PhotoImage(file='infect.png')
btn= Button(window, highlightthickness = 0, bd = 0, width=64, height=62, image=infectbtn, command= add)
btn.place(x=955, y=510)

infec1= Button(window, text="Air Transmission " + str(infectivity_upgrades["air"]+1) + "\nCost: " + str(upgrade_cost_a), height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12), command=air_upgrade)
infec2= Button(window, text="Land Transmission " + str(infectivity_upgrades["land"]+1) + "\nCost: " + str(upgrade_cost_b), height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12), command=land_upgrade)
infec3= Button(window, text="Water Transmission " + str(infectivity_upgrades["water"]+1) + "\nCost: " + str(upgrade_cost_c), height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12), command=water_upgrade)

infec1.place(x=25, y=185)
infec2.place(x=25, y=290)
infec3.place(x=25, y=395)

lethal1= Button(window, text="Symptom: Fever " + str(symptom_upgrades["fever"]+1) + "\nCost: " + str(upgrade_cost_d), height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12), command=fever_upgrade)
lethal2= Button(window, text="Symptom: Cough " + str(symptom_upgrades["cough"]+1) + "\nCost: " + str(upgrade_cost_e), height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12), command=cough_upgrade)
lethal3= Button(window, text="Symptom: Nausea " + str(symptom_upgrades["nausea"]+1) + "\nCost: " + str(upgrade_cost_f), height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12), command=nausea_upgrade)

lethal1.place(x=250, y=185)
lethal2.place(x=250, y=290)
lethal3.place(x=250, y=395)

misc1= Button(window, text="Cure Resistance " + str(misc_upgrades["cure"]+1) + "\nCost: " +str(upgrade_cost_g), height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12), command=cure_upgrade)
misc2= Button(window, text="Mutation Chance ", height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))
misc3= Button(window, text="Tick Speed " +str(misc_upgrades["tick speed"]+1) +"\nCost: " +str(upgrade_cost_h), height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12),command=tick_upgrade)

misc1.place(x=475, y=185)
misc2.place(x=475, y=290)
misc3.place(x=475, y=395)


# Execute tkinter
tick()
window.mainloop()

