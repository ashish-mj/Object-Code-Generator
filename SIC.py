#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 23:31:38 2019

@author: ashish
"""
def binary_convert(num):                                    #binary_conversion
    s=f'{num:04b}'
    return s


def obj_code(op,label,add):
    count=0
    num=opcode[op]                                          #opcode(1-8)
    oc=binary_convert(int(num[0],16))+binary_convert(int(num[1],16))
    for i in range(len(label)):                             #index_bit(9)
        if label[i]==',':
            if label[i+1]=="X":
                count=1
                break
    if count==0:
        oc=oc+'0'
    else:
        oc=oc+'1'
    n=binary_convert(int(add[0],16))                         #address(10-24)
    n=n[1:]
    oc=oc+n
    oc=oc+binary_convert(int(add[1],16))
    oc=oc+binary_convert(int(add[2],16))
    oc=oc+binary_convert(int(add[3],16))                        #binary_format to hexa
    s1=oc[:4]                                                #if wanted tocaps
    s1=hex(int(s1,2))
    s1=s1.upper()
    s2=oc[4:8]
    s2=hex(int(s2,2))
    s2=s2.upper()
    s3=oc[8:12]
    s3=hex(int(s3,2))
    s3=s3.upper()
    s4=oc[12:16]
    s4=hex(int(s4,2))
    s4=s4.upper()
    s5=oc[16:20]
    s5=hex(int(s5,2))
    s5=s5.upper()
    s6=oc[20:]
    s6=hex(int(s6,2))
    s6=s6.upper()
    s=s1[2:]+s2[2:]+s3[2:]+s4[2:]+s5[2:]+s6[2:]
    return s       
######################################################################
opcode={'STL':'14','JSUB':'48','LDA':'00','COMP':'28','STCH':'54','LDCH':'50',\
        "RSUB":"4C","JEQ":"30","J":"3C","STA":"0C","LDL":"08","LDX":"04","TD":"E0",\
        "RD":"D8","TIX":"2C","JLT":"38","STX":"10","WD":"DC",}

def call1(op,label,address):
    op=op.upper()
    label=label.upper()
    address=address.upper()
    if (op=="BYTE" or op=="WORD") and address=="-":                                #Word or byte instruction
      if label[0]=="X":                                       #BYTE X'F1'
        for i in range(len(label)):
            if label[i]=="'":
                return label[i+1:len(label)-1]                                        
      elif label=="C'EOF'":                                   #EOF instruction
          return "454F46"                     
      else:                                                   #WORD 3 example
        label=hex(int(label))    
        return label[2:].upper() 
    elif label=="-" and  address=="-":                          #RSUB - -
      c=opcode[op]+"0000"
      return c 
    
    else:
       try:
           a=obj_code(op,label,address)
           return a
       except KeyError:                                       #RESW or RESB or START
          return "No Object code  for such instruction"  
       except:
          return "INVALID INPUT"                            
    
   