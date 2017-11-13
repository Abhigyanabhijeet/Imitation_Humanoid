from tkinter import *
import serial
import time
import pandas as pd
ssc32 = serial.Serial('COM4', 115200, timeout=1)

m=0
M=180
master = Tk()
C = Canvas(master, bg="blue", height=500, width=280) 
filename = PhotoImage(file = "C:\\Users\\mahe\\Desktop\\servogui\\del.png")
background_label = Label(master, image=filename)
background_label.place(x=250, y=0, relwidth=1, relheight=1)
r=1
ra=1
def show1():
   m=e1.get()
   M=e2.get()
   w = Scale(master, from_=m, to=M, orient=HORIZONTAL,command=here1,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
   w.grid(row=ra,column=1)
def here1(val):
    
    data=str(val)+'a'
    bytes = str.encode(data)
    ssc32.write(bytes)
    print (ssc32.readline())
    ssc32.flush()

var = StringVar()
var2= StringVar()
label = Label( master, textvariable=var, relief=RAISED,bg='CYAN' )
label2=Label(master, textvariable=var2, relief=RAISED,bg='CYAN' )
var.set("Servo1")
var2.set("servo2")
label.grid(row=ra-1, column=1)
label2.grid(row=ra-1, column=7)

e1 = Entry(master,bd =5,width=3)
e2 = Entry(master,bd =5,width=3)
e1.grid(row=ra, column=0)
e2.grid(row=ra, column=3)
w = Scale(master, from_=0, to=180, orient=HORIZONTAL,command=here1,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
w.grid(row=ra,column=1)
Button(master, text='Change', command=show1).grid(row=r, column=4, sticky=W, pady=4)


def show2():
   m2=e3a.get()
   M2=e4a.get()
   w1 = Scale(master, from_=m2, to=M2, orient=HORIZONTAL,command=here2,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
   w1.grid(row=ra,column=7)
def here2(val):
    data=str(val)+'b'
    bytes = str.encode(data)
    ssc32.write(bytes)
    print (ssc32.readline())
    ssc32.flush()
    
e3a = Entry(master,bd =5,width=3)
e4a = Entry(master,bd =5,width=3)
e3a.grid(row=ra, column=6)
e4a.grid(row=ra, column=8)
w1 = Scale(master, from_=0, to=180, orient=HORIZONTAL,command=here2,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
w1.grid(row=ra,column=7)
Button(master, text='Change', command=show2).grid(row=ra, column=9, sticky=W, pady=4)
########################################################
rb=3
def show3():
   m3=e5c.get()
   M3=e6c.get()
   w2 = Scale(master, from_=m3, to=M3, orient=HORIZONTAL,command=here3,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
   w2.grid(row=rb,column=1)
def here3(val):
    data=str(val)+'c'
    bytes = str.encode(data)
    ssc32.write(bytes)
    print (ssc32.readline())
    ssc32.flush()
    
e5c = Entry(master,bd =5,width=3)
e6c = Entry(master,bd =5,width=3)
e5c.grid(row=rb, column=0)
e6c.grid(row=rb, column=3)
w2 = Scale(master, from_=0, to=180, orient=HORIZONTAL,command=here3,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
w2.grid(row=rb,column=1)
Button(master, text='Change', command=show3).grid(row=rb, column=4, sticky=W, pady=4)

var = StringVar()
var2= StringVar()
label = Label( master, textvariable=var, relief=RAISED,bg='CYAN')
label2=Label(master, textvariable=var2, relief=RAISED,bg='CYAN')
var.set("Servo3")
var2.set("servo4")
label.grid(row=rb-1, column=1)
label2.grid(row=rb-1, column=7)

def show4():
   m2q=e3d.get()
   M2q=e4d.get()
   w3 = Scale(master, from_=m2q, to=M2q, orient=HORIZONTAL,command=here4,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
   w3.grid(row=rb,column=7)
def here4(val):
    data=str(val)+'d'
    bytes = str.encode(data)
    ssc32.write(bytes)
    #print (ssc32.readline())
    ssc32.flush()
e3d = Entry(master,bd =5,width=3)
e4d = Entry(master,bd =5,width=3)
e3d.grid(row=rb, column=6)
e4d.grid(row=rb, column=8)
w3 = Scale(master, from_=0, to=180, orient=HORIZONTAL,command=here4,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
w3.grid(row=rb,column=7)
Button(master, text='Change', command=show4).grid(row=rb, column=9, sticky=W, pady=4)
#################################################
#################################################
rc=5
def show5():
   me=e59.get()
   Me=e69.get()
   w4 = Scale(master, from_=me, to=Me, orient=HORIZONTAL,command=here5,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
   w4.grid(row=rc,column=1)
def here5(val):
    data=str(val)+'e'
    bytes = str.encode(data)
    ssc32.write(bytes)
    #print (ssc32.readline())
    ssc32.flush()

var = StringVar()
var2= StringVar()
label = Label( master, textvariable=var, relief=RAISED,bg='CYAN' )
label2=Label(master, textvariable=var2, relief=RAISED,bg='CYAN' )
var.set("Servo5")
var2.set("servo6")
label.grid(row=rc-1, column=1)
label2.grid(row=rc-1, column=7)

e59 = Entry(master,bd =5,width=3)
e69 = Entry(master,bd =5,width=3)
e59.grid(row=rc, column=0)
e69.grid(row=rc, column=3)
w4 = Scale(master, from_=0, to=180, orient=HORIZONTAL,command=here5,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
w4.grid(row=rc,column=1)
Button(master, text='Change', command=show5).grid(row=rc, column=4, sticky=W, pady=4)


def show6():
   mf=e7f.get()
   Mf=e8f.get()
   w5 = Scale(master, from_=mf, to=Mf, orient=HORIZONTAL,command=here6,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
   w5.grid(row=rc,column=7)
def here6(val):
    data=str(val)+'f'
    bytes = str.encode(data)
    ssc32.write(bytes)
    #print (ssc32.readline())
    ssc32.flush()
e7f = Entry(master,bd =5,width=3)
e8f = Entry(master,bd =5,width=3)
e7f.grid(row=rc, column=6)
e8f.grid(row=rc, column=8)
w5 = Scale(master, from_=0, to=180, orient=HORIZONTAL,command=here6,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
w5.grid(row=rc,column=7)
Button(master, text='Change', command=show6).grid(row=rc, column=9, sticky=W, pady=4)
########################################################
rd=7
def show7():
   md=e9.get()
   Md=e10.get()
   w6 = Scale(master, from_=md, to=Md, orient=HORIZONTAL,command=here7,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
   w6.grid(row=rd,column=1)
def here7(val):
    data=str(val)+'g'
    bytes = str.encode(data)
    ssc32.write(bytes)
    #print (ssc32.readline())
    ssc32.flush()
e9 = Entry(master,bd =5,width=3)
e10 = Entry(master,bd =5,width=3)
e9.grid(row=rd, column=0)
e10.grid(row=rd, column=3)
w6 = Scale(master, from_=0, to=180, orient=HORIZONTAL,command=here7,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
w6.grid(row=rd,column=1)
Button(master, text='Change', command=show7).grid(row=rd, column=4, sticky=W, pady=4)

var = StringVar()
var2= StringVar()
label = Label( master, textvariable=var, relief=RAISED ,bg='CYAN')
label2=Label(master, textvariable=var2, relief=RAISED,bg='CYAN' )
var.set("Servo7")
var2.set("servo8")
label.grid(row=rd-1, column=1)
label2.grid(row=rd-1, column=7)

def show8():
   m2=e11.get()
   M2=e12.get()
   w7 = Scale(master, from_=m2, to=M2, orient=HORIZONTAL,command=here8,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
   w7.grid(row=rd,column=7)
def here8(val):
    data=str(val)+'h'
    bytes = str.encode(data)
    ssc32.write(bytes)
    #print (ssc32.readline())
    ssc32.flush()
e11 = Entry(master,bd =5,width=3)
e12= Entry(master,bd =5,width=3)
e11.grid(row=rd, column=6)
e12.grid(row=rd, column=8)
w7 = Scale(master, from_=0, to=180, orient=HORIZONTAL,command=here8,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
w7.grid(row=rd,column=7)
Button(master, text='Change', command=show8).grid(row=rd, column=9, sticky=W, pady=4)
#######################################################
re=9
def show9():
   mw=e13a.get()
   Mw=e14a.get()
   w8 = Scale(master, from_=mw, to=Mw, orient=HORIZONTAL,command=here9,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
   w8.grid(row=re,column=1)
def here9(val):
    data=str(val)+'i'
    bytes = str.encode(data)
    ssc32.write(bytes)
    #print (ssc32.readline())
    ssc32.flush()
e13a = Entry(master,bd =5,width=3)
e14a = Entry(master,bd =5,width=3)
e13a.grid(row=re, column=0)
e14a.grid(row=re, column=3)
w8 = Scale(master, from_=0, to=180, orient=HORIZONTAL,command=here9,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
w8.grid(row=re,column=1)
Button(master, text='Change', command=show9).grid(row=re, column=4, sticky=W, pady=4)

var = StringVar()
var2= StringVar()
label = Label( master, textvariable=var, relief=RAISED,bg='CYAN' )
label2=Label(master, textvariable=var2, relief=RAISED,bg='CYAN' )
var.set("Servo9")
var2.set("servo10")
label.grid(row=re-1, column=1)
label2.grid(row=re-1, column=7)

def show10():
   m2z=e15.get()
   M2z=e16.get()
   w9 = Scale(master, from_=m2z, to=M2z, orient=HORIZONTAL,command=here10,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
   w9.grid(row=re,column=7)
def here10(val):
    data=str(val)+'j'
    bytes = str.encode(data)
    ssc32.write(bytes)
    #print (ssc32.readline())
    ssc32.flush()
e15 = Entry(master,bd =5,width=3)
e16= Entry(master,bd =5,width=3)
e15.grid(row=re, column=6)
e16.grid(row=re, column=8)
w9 = Scale(master, from_=0, to=180, orient=HORIZONTAL,command=here10,activebackground='RED',bg='WHITE',bd=5,highlightbackground='BLACK',highlightcolor='RED',troughcolor='BLACK')
w9.grid(row=re,column=7)
Button(master, text='Change', command=show10).grid(row=re, column=9, sticky=W, pady=4)
######################
#####################
df=pd.read_csv('datapoints.csv')
df=df.set_index('Id')
def Set_Initial():
    df.set_value('a', 'Mov',w.get())
    df.set_value('b', 'Mov',w1.get())
    df.set_value('c', 'Mov',w2.get())
    df.set_value('d', 'Mov',w3.get())
    df.set_value('e', 'Mov',w4.get())
    df.set_value('f', 'Mov',w5.get())
    df.set_value('g', 'Mov',w6.get())
    df.set_value('h', 'Mov',w7.get())
    df.set_value('i', 'Mov',w8.get())
    df.set_value('j', 'Mov',w9.get())
    df.to_csv('datapoints.csv')
    print(df)

def Get_Initial():
   w.set(df['Mov']['a'])
   w1.set(df['Mov']['b'])
   
   w2.set(df['Mov']['c'])
   w3.set(df['Mov']['d'])
   
   w4.set(df['Mov']['e'])
   w5.set(df['Mov']['f'])
   
   w6.set(df['Mov']['g'])
   w7.set(df['Mov']['h'])
   
   w8.set(df['Mov']['i'])
   w9.set(df['Mov']['j'])


def Frame():
    framenos=df.at["framedata","Variables"]
    name ='frame'+str(framenos)
    df.set_value('a', name,w.get())
    df.set_value('b', name,w1.get())
    df.set_value('c', name,w2.get())
    df.set_value('d', name,w3.get())
    df.set_value('e', name,w4.get())
    df.set_value('f', name,w5.get())
    df.set_value('g', name,w6.get())
    df.set_value('h', name,w7.get())
    df.set_value('i', name,w8.get())
    df.set_value('j', name,w9.get())
    framenos +=1
    df.set_value('framedata', 'Variables',framenos)
    df.to_csv('datapoints.csv')
    print(df)   

def LoadFrame():
   x=e.get()
   myname='frame'+str(float(x))
   w.set(df[myname]['a'])
   w1.set(df[myname]['b'])
   w2.set(df[myname]['c'])
   w3.set(df[myname]['d'])
   w4.set(df[myname]['e'])
   w5.set(df[myname]['f'])
   w6.set(df[myname]['g'])
   w7.set(df[myname]['h'])
   w8.set(df[myname]['i'])
   w9.set(df[myname]['j'])

def EditFrame():
   xd=f.get()
   nam='frame'+str(float(xd))
   df.set_value('a', nam,w.get())
   df.set_value('b', nam,w1.get())
   df.set_value('c', nam,w2.get())
   df.set_value('d', nam,w3.get())
   df.set_value('e', nam,w4.get())
   df.set_value('f', nam,w5.get())
   df.set_value('g', nam,w6.get())
   df.set_value('h', nam,w7.get())
   df.set_value('i', nam,w8.get())
   df.set_value('j', nam,w9.get())
   df.to_csv('datapoints.csv')
   print(df)

Button(master, text='Set Initial Value', command=Set_Initial,bg='MAGENTA').grid(row=11, column=1, sticky=W, pady=4)
Button(master, text='INITIALIZE', command=Get_Initial,bg='LIME').grid(row=11, column=7, sticky=W, pady=4)
Button(master, text='Set New Frame', command=Frame,bg='SKYBLUE').grid(row=13, column=1, sticky=W, pady=4)
Button(master, text='Load Frame', command=LoadFrame,bg='SKYBLUE').grid(row=13, column=4, sticky=W, pady=4)
Button(master, text='Set Old Frame', command=EditFrame,bg='SKYBLUE').grid(row=13, column=7, sticky=W, pady=4)

e = Entry(master,bd =5,width=3)
e.grid(row=13, column=3)
f = Entry(master,bd =5,width=3)
f.grid(row=13, column=6)

var = StringVar()
var2= StringVar()
label = Label( master, textvariable=var, relief=RAISED,bg='CYAN' )
label2=Label(master, textvariable=var2, relief=RAISED,bg='CYAN' )
var.set("Frame NUM")
var2.set("Frame NUM")
label.grid(row=12, column=3)
label2.grid(row=12, column=6)
###############################################
'''make a move'''

def LoadFrameMove(myname):
   w.set(df[myname]['a'])
   w1.set(df[myname]['b'])
   w2.set(df[myname]['c'])
   w3.set(df[myname]['d'])
   w4.set(df[myname]['e'])
   w5.set(df[myname]['f'])
   w6.set(df[myname]['g'])
   w7.set(df[myname]['h'])
   w8.set(df[myname]['i'])
   w9.set(df[myname]['j'])



def play():
   stri=move.get()
   delay=delt.get()
   stri = stri.replace(',', '0')
   l = list(stri)
   for element in l:
      if(element!='0'):
         myname='frame'+str(float(element))
         LoadFrameMove(myname)
         time.sleep(int(delay))
         print("stepdone")
var3 = StringVar()
label3 = Label( master, textvariable=var3, relief=RAISED,bg='CYAN' )
var3.set("Move")
label3.grid(row=14, column=0)
move = Entry(master,bd =5,width=3)
move.grid(row=14, column=3)
Button(master, text='Play', command=play,bg='SKYBLUE').grid(row=14, column=4, sticky=W, pady=4)

va= StringVar()
label4 = Label( master, textvariable=va, relief=RAISED,bg='CYAN' )
va.set("delay")
label4.grid(row=14, column=5)

delt = Entry(master,bd =5,width=3)
delt.grid(row=14, column=6)


mainloop( )
