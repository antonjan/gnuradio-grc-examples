#!/usr/bin/env python

from Tkinter import *
from PIL import ImageTk, Image
import os


# Simple UI voor LEANDVB, DVBS receiver.
# requires sudo apt-get install python-imaging-tk package
# keep everything in same directory where leandvb is
# if you add a 180x180 pixels file called logo.jpg it will be
# showed in richt corner.
# pe2jko@540.org

master = Tk()
master.title('LeanDVB interface')



parameters = ""
lengte=0
parameter1_conv1=0
parameter2_conv2=0
parameter3_conv3= ""
if os.path.isfile("leanlastrun"):
    file = open("leanlastrun", "r")
    parameter1 = file.readline() #freq
    parameter2 = file.readline() #samplerate
    parameter3 = file.readline() #fec
    parameter6 = file.readline() #tune
    parameter4 = file.readline() #fastlock
    parameter5 = file.readline() #lowsr
    parameter7 = file.readline() #viterbi
    parameter8 = file.readline() #Gui
    parameter9 = file.readline() #No preprocessin
    parameter10 = file.readline() #max sensitive
    parameter11 = file.readline() #hard-metric
    parameter12 = file.readline() #rtl0
    parameter13 = file.readline() #rtl1
    parameter14 = file.readline() #pad leandvb
    parameter15 = file.readline() #ppm
    parameter1_conv1 = str(parameter1[:-1])
    parameter2_conv2 = int(parameter2)
    parameter3_conv3 = str(parameter3[:3])
    parameter4_conv4 = int (parameter6)
    file.close()
else:
    parameter1_conv1 = 1280
    parameter2_conv2 = 500
    parameter3_conv3 = "5/6"
    parameter4_conv4 = 0
    parameter1 = "1280"
    parameter2 = "500"
    parameter3 = 1
    parameter4 = 1
    parameter5 = 1
    parameter6 = 0
    parameter7 = 0
    parameter8 = 1
    parameter9 = 0
    parameter10 = 0
    parameter11 = 0
    parameter12 = 1
    parameter13 = 0
    parameter14 = "leandvb."
    parameter15 = 1
    
var1 = IntVar()
#Checkbutton(master, font = "Verdana 13 italic", text="Fastlock", variable=var1).grid(row=5, sticky=W)
Checkbutton(master, font = "Verdana 12", text="Fastlock", variable=var1).grid(row=5, sticky=W)
var2 = IntVar()
Checkbutton(master, font = "Verdana 12" ,text="Low SR", variable=var2).grid(row=5, column=1, sticky=W)
var3 = IntVar()
Checkbutton(master, font = "Verdana 12" ,text="Viterbi", variable=var3).grid(row=5, column=1, sticky=E)
var4 = IntVar()
Checkbutton(master, font = "Verdana 12" ,text="Hard-Metric", variable=var4).grid(row=5, column=1)

Label(master,font = "Verdana 10 italic", text="-----------------------").grid(row=4,column=0)
Label(master,font = "Verdana 10 italic", text="---------------------------------------------------------").grid(row=4,column=1)
var5 = IntVar()
Checkbutton(master, font = "Verdana 13", text="Gui", variable=var5).grid(row=7, sticky=W)
var6 = IntVar()
Checkbutton(master, font = "Verdana 13" ,text="No Pre-Processing", variable=var6).grid(row=7, column=1, sticky=W)
var7 = IntVar()
Checkbutton(master, font = "Verdana 13" ,text="Max sensitive", variable=var7).grid(row=7, column=1, sticky=E)
Label(master,font = "Verdana 8 italic", text="").grid(row=6,column=0)
Label(master,font = "Verdana 8 italic", text="").grid(row=8,column=0)

rtl0 = IntVar()
rtl1 = IntVar()
ppm = IntVar()
padlean = StringVar()

var1.set(int(parameter4))
var2.set(int(parameter5))
var3.set(int(parameter7))
var4.set(int(parameter11))
var5.set(int(parameter8))
var6.set(int(parameter9))
var7.set(int(parameter10))
rtl0.set(int(parameter12))
rtl1.set(int(parameter13))
padlean.set(str(parameter14[:-1]))
ppm.set(int(parameter15))

e = Entry(master, font = "Verdana 15 bold")
f = Entry(master, font = "Verdana 15 bold")
g = Entry(master, font = "Verdana 15 bold")
h = Entry(master, font = "Verdana 15 bold")
e.insert(0, parameter1_conv1)
f.insert(0, parameter2_conv2)
g.insert(0, parameter3_conv3)
h.insert(0, parameter4_conv4)
e.grid(row=0, column=1)
f.grid(row=1, column=1)
g.grid(row=2, column=1)
h.grid(row=3, column=1)


e.focus_set()
if os.path.isfile("logo.jpg"):
    im = Image.open('logo.jpg')
    photo = ImageTk.PhotoImage(im)
    label = Label(image=photo)
    label.image = photo
    label.grid(row=0, column=3, columnspan=2, rowspan=3,sticky=W+E+N+S, padx=5, pady=5)

def einde():
    master.destroy()



def preset1():
    top = Toplevel()
    top.title("Default Settings")
    top.geometry("300x200+30+30")    
    top.transient(master)
    C1 = Checkbutton(top, font = "Verdana 11 italic", text="RTL=0", variable=rtl0)
    C1.pack()
    C2 = Checkbutton(top, font = "Verdana 11 italic", text="RTL=1", variable=rtl1)
    C2.pack()
    kk= Label(top, font = "Verdana 10", text="Path to Leansdr :")
    kk.pack()
    i = Entry(top, font = "Verdana 10", width=35, textvariable=padlean)
    i.pack()
    kl= Label(top, font = "Verdana 10", text="------------")
    kl.pack()
    kk= Label(top, font = "Verdana 10", text="PPM offset RTL0")
    kk.pack() 
    j = Entry(top, font = "Verdana 10", width=15, textvariable=ppm)
    j.pack()
    km= Label(top, font = "Verdana 10", text="------------")
    km.pack()
    topButton = Button(top, text="CLOSE", command = top.destroy)
    topButton.pack()


def save_parms():
    sub = ""
    samplerate = 0
    freq = 0
    tune = 0
    fastlock = var1.get()
    lowsr = var2.get()
    viterbi = var3.get()
    gui = var5.get()
    nopreprocess = var6.get()
    maxprocess = var7.get()
    hardmetric = var4.get()
    rtldongle0 = rtl0.get()
    rtldongle1 = rtl1.get()
    leanpad = padlean.get()
    srsubstring = f.get()
    tunesubstring = str(1)
    opslaanfreq= e.get()
    fsubstring = float(e.get())
    tunesubstring = str(1)
    freq = fsubstring * 1000000
    freqfinal=int(freq)
    samplerate = int(srsubstring) * 1000
    fec = tkvar3.get()
    tune = h.get()
    ppmwaarde = ppm.get()
    file = open("runlean", "w")
    file.write("#!/bin/sh \n\n")
    file.write(sub)
    file.close()
    file = open("leanlastrun", "w")
    file.write(str(opslaanfreq) + "\n")    
    file.write(srsubstring + "\n")
    file.write(fec + "\n")
    file.write(tune + "\n")
    file.write(str(fastlock) + "\n")
    file.write(str(lowsr) + "\n")
    file.write(str(viterbi) + "\n")
    file.write(str(gui) + "\n")
    file.write(str(nopreprocess) + "\n")
    file.write(str(maxprocess) + "\n")
    file.write(str(hardmetric) + "\n")
    file.write(str(rtldongle0) + "\n")
    file.write(str(rtldongle1) + "\n")
    file.write(str(leanpad) + "\n")
    file.write(str(ppmwaarde) + "\n")
    file.write(tunesubstring + "\n")
    file.close()

def callback():
    ppmwaarde = ppm.get()
    sub = ""
    samplerate = 0
    freq = 0
    tune = 0
    fastlock = var1.get()
    lowsr = var2.get()
    viterbi = var3.get()
    gui = var5.get()
    nopreprocess = var6.get()
    maxprocess = var7.get()
    hardmetric = var4.get()
    rtldongle0 = rtl0.get()
    rtldongle1 = rtl1.get()
    leanpad = padlean.get()
    if (lowsr == 1):
        bandbreedte = 1024000
    else:
        bandbreedte = 2400000
    if (fastlock == 1):
        fastlockstring = "--fastlock"
    else:
        fastlockstring = ""
    if (viterbi == 1):
        viterbistring = "--viterbi"
    else:
        viterbistring = ""
    if (gui == 1):
        guistring = "--gui"
    else:
        guistring = ""
    if (nopreprocess == 1):
        nopreprocessstring = "--hs"
    else:
        nopreprocessstring = ""
    if (maxprocess == 1):
        maxprocessstring = "--hq"
    else:
        maxprocessstring = ""
    if (hardmetric == 1):
        hardmetricstring = "--hard-metric"
    else:
        hardmetricstring = ""
    if (rtldongle0 == 1):
        rtlstring = "0"
    else:
        rtlstring = "1"        
    srsubstring = f.get()
    opslaanfreq= e.get()
    fsubstring = float(e.get())
    tunesubstring = str(1)
    freq = fsubstring * 1000000
    freqfinal=int(freq)
    samplerate = int(srsubstring) * 1000
    fec = tkvar3.get()
    tune = h.get()

    sub = "rtl_sdr -d " + rtlstring + " -f "  + str(freqfinal) + " -s " + str(bandbreedte) + " -p " + str(ppmwaarde) + " - | " + str(leanpad) + " " + guistring + " " + maxprocessstring + " "+ nopreprocessstring + " " + viterbistring + " " + hardmetricstring + " " + fastlockstring + " --tune " + tune + " --cr " + str(fec) + " --sr " + str(samplerate) + " -f " + str(bandbreedte) + " | ffplay -v 0 - \n" 

    file = open("runlean", "w")
    file.write("#!/bin/sh \n\n")
    file.write(sub)
    file.close()
    file = open("leanlastrun", "w")
    file.write(str(opslaanfreq) + "\n")    
    file.write(srsubstring + "\n")
    file.write(fec + "\n")
    file.write(tune + "\n")
    file.write(str(fastlock) + "\n")
    file.write(str(lowsr) + "\n")
    file.write(str(viterbi) + "\n")
    file.write(str(gui) + "\n")
    file.write(str(nopreprocess) + "\n")
    file.write(str(maxprocess) + "\n")
    file.write(str(hardmetric) + "\n")
    file.write(str(rtldongle0) + "\n")
    file.write(str(rtldongle1) + "\n")
    file.write(str(leanpad) + "\n")
    file.write(str(ppmwaarde) + "\n")
    file.write(tunesubstring + "\n")
    file.close()
    os.system("sh ./runlean")

Button(master,font = "Verdana 11 italic", text='EXIT', command=einde).grid(row=7, column=3,sticky=E)
Button(master, font = "Verdana 11 italic",highlightbackground='red',text='START', command=callback).grid(row=7, column=3,sticky=W)
Button(master, font = "Verdana 11 italic",fg='red',highlightbackground='blue',text='Default Settings', command=preset1).grid(row=3, column=3)
Button(master, font = "Verdana 11 italic",fg='red',highlightbackground='blue',text='  Save Settings ', command=save_parms).grid(row=5, column=3)
#Button(master, font = "Verdana 9 italic",fg='red',highlightbackground='blue',text='UI options', command=preset3).grid(row=2, column=5, ipady=5,sticky=E, ipadx=5)
#Button(master, font = "Verdana 9 italic",fg='red',highlightbackground='blue',text='General Options', command=preset4).grid(row=3, column=5, ipady=5,sticky=E,ipadx=5)

tkvar1 = StringVar(master)
 
# Frequency Dropdown
choices1 = { '1252','1257','1260','436','437','1255','1252.600','1280','1250','1253'}

tkvar1.set(parameter1[:-1]) # set the default option
 
popupMenu = OptionMenu(master, tkvar1, *choices1)
Label(master, text=" Frequency ", font = "Verdana 14 italic").grid(row = 0, column = 0)
Label(master, text="MHz", font = "Verdana 14 italic").grid(row = 0, column = 2,sticky=W)
popupMenu.grid(row = 0, column =1, sticky=E)
 
# on change dropdown value
def change_dropdown1(*args):
    print( tkvar1.get() )
    e.delete(0, END)
    e.insert(0, tkvar1.get())
    
 
# link function to change dropdown
tkvar1.trace('w', change_dropdown1)

tkvar2 = StringVar(master)
 
# SampleRate
choices2 = { '125','150','250','333','400','500','600','750','1000','1500','2000','2083','3000','4000','4340','5000'}

tkvar2.set(parameter2[:-1]) # set the default option
 
popupMenu = OptionMenu(master, tkvar2, *choices2)
Label(master, text=" Samplerate ", font = "Verdana 14 italic").grid(row = 1, column = 0)
Label(master, text="S/R", font = "Verdana 14 italic").grid(row = 1, column = 2,sticky=W)
popupMenu.grid(row = 1, column =1, sticky=E)
 
# on change dropdown value
def change_dropdown2(*args):
    print( tkvar2.get() )
    f.delete(0, END)
    f.insert(0, tkvar2.get())
    
 
# link function to change dropdown
tkvar2.trace('w', change_dropdown2)


tkvar3 = StringVar(master)
# Fec
choices3 = { '1/2','2/3','3/4','5/6','7/8'}
tkvar3.set(parameter3_conv3) # set the default option
 
popupMenu = OptionMenu(master, tkvar3, *choices3)
Label(master, text="FEC", font = "Verdana 14 italic").grid(row = 2, column = 0)
Label(master, text="Div", font = "Verdana 14 italic").grid(row = 2, column = 2,sticky=W)
popupMenu.grid(row = 2, column =1, sticky=E)
 
# on change dropdown value
def change_dropdown3(*args):
    print(  )
    g.delete(0, END)
    g.insert(0, tkvar3.get())
    
 
# link function to change dropdown
tkvar3.trace('w', change_dropdown3)

tkvar4 = StringVar(master)
# Tune
choices4 = { '100','500','1000','2000','5000','10000','-100','-500','-1000','-2000','-5000','-10000'}
tkvar4.set(parameter4_conv4) # set the default option
 
popupMenu = OptionMenu(master, tkvar4, *choices4)
Label(master, text="Tune", font = "Verdana 14 italic").grid(row = 3, column = 0)
Label(master, text="Hz", font = "Verdana 14 italic").grid(row = 3, column = 2,sticky=W)
popupMenu.grid(row = 3, column =1, sticky=E)
 
# on change dropdown value
def change_dropdown4(*args):
    print(  )
    h.delete(0, END)
    h.insert(0, tkvar4.get())
    
 
# link function to change dropdown
tkvar4.trace('w', change_dropdown4)


mainloop()


