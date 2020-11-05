#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 15:18:09 2019

@author: ashish
"""
import tkinter as tk
import SIC as s
import XE as x

output = ''          #sic global variables
op=""
operand=""
address=""

output1 = ''          #sic_xe global variables
op1=""              
operand1=""
address1=""
pc=""
b=""


def clear_sic():
    global op
    global operand
    global address
    global output
    op.delete(0,tk.END)
    operand.delete(0,tk.END)
    address.delete(0,tk.END)
    output.config(text="Enter the Inputs")
    
    
def clear_sicxe():
    global op1
    global operand1
    global address1
    global pc
    global b
    global output1
    op1.delete(0,tk.END)
    operand1.delete(0,tk.END)
    address1.delete(0,tk.END)
    pc.delete(0,tk.END)
    b.delete(0,tk.END)
    output1.config(text="Enter the Inputs")
    
def sic():
    sub = tk.Tk()                                         #create window
    sub.title("SIC")
    L1 = tk.Label(sub, text = "Mnemonic opcode",font=("Bitstream Charter",15," bold"))
    L1.place(x=254,y=270 )
    global op
    op=tk.Entry(sub,font=("Bitstream Charter",14," bold"),width=15)
    op.place(x=256,y=300)
    L2 = tk.Label(sub, text = "Operand",font=("Bitstream Charter",15," bold"))
    L2.place(x=595,y=270 )
    global operand
    operand=tk.Entry(sub,font=("Bitstream Charter",14," bold"),width=15)
    operand.place(x=553,y=300)
    L3= tk.Label(sub, text = "Operand Address",font=("Bitstream Charter",15," bold"))
    L3.place(x=859,y=270 )
    global address
    address=tk.Entry(sub,font=("Bitstream Charter",14," bold"),width=15)
    address.place(x=857,y=300)
    button1 = tk.Button(sub,text='GENERATE',bg="green",fg="white",font=("Courier 10 Pitch",17,"bold ")\
             ,width=10,height=1,border=2,relief="raised",command=update_answer_sic)
    button1.place(x=550,y=400)
    button2 = tk.Button(sub,text='CLEAR',bg="red",fg="white",font=("Courier 10 Pitch",17,"bold ")\
             ,width=10,height=1,border=2,relief="raised",command=lambda :clear_sic())
    button2.place(x=550,y=450)
    L4= tk.Label(sub, text = "NOTE: Enter empty field with '-'",font=("Bitstream Charter",15,"bold italic"),fg="red")
    L4.place(x=500,y=350 )
    global output
    output=tk.Label(sub,text="Enter the Inputs",width=38,font=("Courier 10 Pitch",25,"bold italic"),bg="black",fg="green")
    output.place(x=260,y=140)
    sub.mainloop()
    
def update_answer_sic():
    global op
    global operand
    global address
    result=s.call1(op.get(),operand.get(),address.get())
    global output
    output.config(text='{}'.format(result))
 
def sicxe():
    sub1 = tk.Tk()                                         #create window
    sub1.title("SIC/XE")
    L1 = tk.Label(sub1, text = "Mnemonic opcode",font=("Bitstream Charter",15," bold"))
    L1.place(x=45,y=270 )
    global op1
    op1=tk.Entry(sub1,font=("Bitstream Charter",14," bold"),width=15)
    op1.place(x=50,y=300)
    L2 = tk.Label(sub1, text = "Operand",font=("Bitstream Charter",15," bold"))
    L2.place(x=345,y=270 )
    global operand1
    operand1=tk.Entry(sub1,font=("Bitstream Charter",14," bold"),width=15)
    operand1.place(x=305,y=300)
    L3 = tk.Label(sub1, text = "Operand Address",font=("Bitstream Charter",15," bold"))
    L3.place(x=550,y=270 )
    global address1
    address1=tk.Entry(sub1,font=("Bitstream Charter",14," bold"),width=15)
    address1.place(x=550,y=300)
    L4= tk.Label(sub1, text ="PC address" ,font=("Bitstream Charter",15," bold"))
    L4.place(x=850,y=270 )
    global pc
    pc=tk.Entry(sub1,font=("Bitstream Charter",14," bold"),width=15)
    pc.place(x=825,y=300)
    L5= tk.Label(sub1, text ="Base address" ,font=("Bitstream Charter",15," bold"))
    L5.place(x=1105,y=270 )
    global b
    b=tk.Entry(sub1,font=("Bitstream Charter",14," bold"),width=15)
    b.place(x=1080,y=300)
    button1 = tk.Button(sub1,text='GENERATE',bg="green",fg="white",font=("Courier 10 Pitch",17,"bold "),\
            width=10,height=1,border=2,relief="raised",command=update_answer_xe)
    button1.place(x=550,y=400)
    button2 = tk.Button(sub1,text='CLEAR',bg="red",fg="white",font=("Courier 10 Pitch",17,"bold ")\
             ,width=10,height=1,border=2,relief="raised",command=lambda :clear_sicxe())
    button2.place(x=550,y=450)
    L6= tk.Label(sub1, text = "NOTE: Enter empty field with '-'",font=("Bitstream Charter",15,"bold italic"),fg="red")
    L6.place(x=500,y=350 )
    global output1
    output1=tk.Label(sub1,text="Enter the Inputs",width=39,font=("Courier 10 Pitch",25,"bold italic"),bg="black",fg="green")
    output1.place(x=260,y=140)
    sub1.mainloop()
    
def update_answer_xe():
    global op1
    global operand1
    global address1
    global pc
    global b
    result=x.call2(op1.get(),operand1.get(),address1.get(),pc.get(),b.get())
    global output1
    output1.config(text='{}'.format(result))    


if __name__== "__main__" :
    root = tk.Tk()                                         #create window
    root.title("OCG")                                     #title
    background = tk.PhotoImage(file="background.png")
    w1 = tk.Label(root, image=background)                  #background image
    w1.place(x=0,y=0,relwidth=1,relheight=1)
    logo= tk.PhotoImage(file="designer.png")
    w2 = tk.Label(root, image=logo,bg="white",anchor='nw',fg="black",text="OBJECT CODE GENERATOR",compound = "left",font=("Courier 10 Pitch",35,"bold italic"),padx=10,pady=5).pack(fill="both")
    button_image= tk.PhotoImage(file="binary-code.png")
    button1 = tk.Button(root,image=button_image,text='SIC',width=200,height=200,bg="white",font=("Courier 10 Pitch",25,"bold "),compound="left",border=20,relief="groove",command=lambda :sic())
    button1.place(x=270,y=250)
    button2 = tk.Button(root,image=button_image,text='SIC/XE',width=200,height=200,bg="white",font=("Courier 10 Pitch",25,"bold"),compound="left",border=20,relief="groove",command=lambda :sicxe())
    button2.place(x=720,y=250)
    student=tk.PhotoImage(file="man.png")
    w4=tk.Label(root,text="Ashish M J\n4NI17IS017",image=student,font=("Bitstream Charter",15,"italic bold"),bg="white",compound="left",padx=10,pady=5,anchor="s",width=770)
    w4.place(x=250,y=650)
    root.mainloop()

 
