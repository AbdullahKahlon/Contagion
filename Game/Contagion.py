#Import Modules
from tkinter import *
from time import sleep
import threading
import datetime
import math
import random

global infections
global multiplier
global infectivity
global count
global currentdate
global points
global upgrade_cost_a
global upgrade_cost_b
global upgrade_cost_c
global upgrade_cost_d
global upgrade_cost_e
global upgrade_cost_f
global upgrade_cost_g
global upgrade_cost_h
global infectivity_upgrades
global symptom_upgrades
global misc_upgrades
global lethality
global mutation
global population
global cure
global dayspassed
global deadpop
global tickspeed
global alivepop
mutation = 0.001
lethality = 0.001
misc_upgrades = {"cure": 0, "mutation": 0, "tick speed": 0}
symptom_upgrades = {"nausea": 0, "cough": 0, "fever": 0}
infectivity_upgrades = {"air": 0, "land": 0, "water": 0}
upgrade_cost_a = 4
upgrade_cost_b = 16
upgrade_cost_c = 64
upgrade_cost_d = 3
upgrade_cost_e = 9
upgrade_cost_f = 27
upgrade_cost_g = 1000
upgrade_cost_h = 1000
infections = -1
tickspeed = 1
infectivity = 1
multiplier = 1
points = 4
infc_per_pnt = 25
count = 0
currentdate = ''
population = 8011626402
cure = 0
dayspassed = 0
deadpop = 0
alivepop = population

def add():
    global infections
    global infectivity
    global points
    global infc_per_pnt
    global cure
    print("a")
    infections += 1*infectivity
    points += (1/infc_per_pnt)*infectivity+(0.1*cure)
    pnts.configure(text=("Points: " + str(math.floor(points))))
    infc.configure(text=("Infections: " + str(math.floor(infections))))
    
def air_upgrade():
    global points
    global infectivity
    global lethality
    global infectivity_upgrades
    global upgrade_cost_a
    global infc_per_pnt

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
    global points
    global infectivity
    global lethality
    global infectivity_upgrades
    global upgrade_cost_b
    global infc_per_pnt
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
    global points
    global infectivity
    global lethality
    global infectivity_upgrades
    global upgrade_cost_c
    global infc_per_pnt
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
    global points
    global lethality
    global symptom_upgrades
    global upgrade_cost_d
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
    global points
    global lethality
    global symptom_upgrades
    global upgrade_cost_f
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
    global points
    global lethality
    global symptom_upgrades
    global upgrade_cost_e
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
    global points
    global cure
    global upgrade_cost_g
    global misc_upgrades

    if points >= upgrade_cost_g:
        misc_upgrades["cure"] += 1
        points -= upgrade_cost_g
        cure -= 10
        upgrade_cost_g *=10
    pnts.configure(text=("Points: " + str(math.floor(points))))

def tick_upgrade():
    global points
    global cure
    global upgrade_cost_h
    global misc_upgrades
    global tickspeed

    if points >= upgrade_cost_h:
        misc_upgrades["tick speed"] += 1
        points -= upgrade_cost_h
        tickspeed -= 0.17
        upgrade_cost_h *=10
    pnts.configure(text=("Points: " + str(math.floor(points))))
    
 
def tick():
    global count
    global infections
    global infectivity
    global currentdate
    global infc
    global points
    global infc_per_pnt
    global population
    global infectivity_upgrades
    global upgrade_cost_a
    global upgrade_cost_b, upgrade_cost_c
    global cure
    global dayspassed
    global deadpop
    global tickspeed
    dayspassed += 1
    
    if dayspassed > 0:
        cure += round(random.uniform(-0.33, 0.66), 3)
    cure_prog.configure(text=("Cure Progress: " + str(round(cure,3)) + "%"))

    deadpop += infections*lethality
    livingpop = population - deadpop
    infections -= infections*lethality
    population -= infections*lethality

    print("t")
    
    infections += infectivity
    infc.configure(text=("Infections: " + str(math.floor(infections))))
    points += ((1/infc_per_pnt)*infectivity)+(cure*1.07)  
    pnts.configure(text=("Points: " + str(math.floor(points))))
    
    uninfecpop = livingpop-infections
    if uninfecpop <= 0:
        infectivity = 0
        infections = population
    else:
        unfecpop.configure(text=("Population Uninfected: " + str(math.floor(livingpop - infections))))
    
    alivepop.config(text=("Population Alive: " + str(math.floor(population-deadpop))))
    drate.config(text=("Deaths per day: " + str(round(infections*lethality,2))))

    count+=1
    currentdate = datetime.date.today() + datetime.timedelta(days=count)
    datelbl.configure(text=("Date: " + str(currentdate)))
    
    lethalitylbl.config(text =("Lethality: " + str(round(lethality*100,2)) + "%"))    
    irate.configure(text=("Infections per day: " + str(round(infectivity,2))))

    misc1.config(text="Cure Resistance " + str(misc_upgrades["cure"]+1) + "\nCost: " +str(upgrade_cost_g))
    misc3.config(text="Tick Speed " +str(misc_upgrades["tick speed"]+1) +"\nCost: " +str(upgrade_cost_h))

    
    
    


    sleep(tickspeed)
    t = threading.Timer(tickspeed, tick)
    t.start()


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
global infc
global pnts
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

