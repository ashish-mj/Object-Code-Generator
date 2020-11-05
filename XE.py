#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 17:06:35 2019

@author: ashish
"""
def binary_convert(num):                                    #binary_conversion
    s=f'{num:04b}'
    return s

def tohex(val,nbits):                                      #convert negative hexa
    return hex((val+(1<<nbits)) % (1<<nbits))              #backward referencing

def check_f1(op):                                     #check format1
    if (op=="FIX" or op=="FLOAT" or op=="HIO" or op=="NORM" or op=="SIO" or op=="TIO"):
        return True
                                              
def check_f2(op):                                    #check format2
    if (op=="ADDR" or op=="CLEAR" or op=="COMPR" or op=="DIVR" or op=="MULR" or \
        op=="RMO" or op=="SHIFTL" or op=="SHIFTR" or op=="SUBR" or op=="SVC" or op=="TIXR"):
        return True

def check_f4(op):                                   #check format4
    if(op[0]=="+"):
        return True
 
def check_PC(add,next_add):
    disp=int(add,16)-int(next_add,16)                                 #check program counter
    if (disp>=-2048 and disp<=2047):
        return True
 
def check_base(add,base_add):
    disp=int(add,16)-int(base_add,16)
    if (disp>=0 and disp<=4095):
        return True
    
def format1(op):                                   #object code if format1
    obj=opcodeF1[op] 
    return obj

def format2(op,label):                             #object code if format2
    obj=opcodeF2[op]
    if (len(label)==1):
        obj=obj+register[label]+"0"
        return obj
    else:
        obj=obj+register[label[0]]+register[label[2]]
        return obj
        
def format3(op,label,add,next_add,base_add):         #object code if format3
    num=opcodeF3nF4[op]
    oc=binary_convert(int(num[0],16))             
    temp=binary_convert(int(num[1],16))          #opcode 2 bit only
    oc=oc+temp[:2]
    
    if(label[0]=="#"):                          #####immediate lda #3
       oc=oc+"010"
       if(label[1:].isdigit()):
           oc=oc+"000"
           temp=label[1:]
           temp=hex(int(temp))
           temp=temp[2:]
           n=len(temp)
           if (n==1):
               temp="0"+"0"+temp
           if (n==2):
               temp="0"+temp
           oc=oc+binary_convert(int(temp[0],16))+binary_convert(int(temp[1],16))+\
           binary_convert(int(temp[2],16))
           return convertF3(oc)
       else:
            if(check_PC(add,next_add)):                     #pc relative addressing
               oc=oc+"010"                         #immediate ldx #length
               disp=int(add,16)-int(next_add,16)
               if disp<0:                              #check backward reference
                  disp=tohex(disp,12)
                  disp=disp[2:]
               else:
                  disp=hex(disp)
                  disp=disp[2:]
               n=len(disp)
               if(n==1):
                   oc=oc+"00000000"+binary_convert(int(disp),16)
                   return convertF3(oc)
               elif (n==2):
                   oc=oc+"0000"+binary_convert(int(disp[0],16))+binary_convert(int(disp[1],16))
                   return convertF3(oc)
               else:
                   oc=oc+binary_convert(int(disp[0],16))+binary_convert(int(disp[1],16))+\
                   binary_convert(int(disp[2],16))
                   return convertF3(oc)
            else:
               if(check_base(add,base_add)):
                    oc=oc+"010"
                    disp=int(add,16)-int(base_add,16)
                    if disp<0:                              #check backward reference
                      disp=tohex(disp,12)
                      disp=disp[2:]
                    else:
                       disp=hex(disp)
                       disp=disp[2:]
                    n=len(disp)
                    if(n==1):
                       oc=oc+"00000000"+binary_convert(int(disp,16))
                       return convertF3(oc)
                    elif (n==2):
                       oc=oc+"0000"+binary_convert(int(disp[0],16))+binary_convert(int(disp[1],16))
                       return convertF3(oc)
                    else:
                        oc=oc+binary_convert(int(disp[0],16))+binary_convert(int(disp[1],16))+\
                   binary_convert(int(disp[2],16)) 
                        return convertF3(oc)
               else:
                    return "ERROR"
    
    elif(label[0]=="@"):              #######################Indirect addressing
        oc=oc+"100"
        if(check_PC(add,next_add)):                     #pc relative addressing
               oc=oc+"010"                         # ldx @length
               disp=int(add,16)-int(next_add,16)
               if disp<0:                              #check backward reference
                  disp=tohex(disp,12)
                  disp=disp[2:]
               else:
                  disp=hex(disp)
                  disp=disp[2:]
               n=len(disp)
               if(n==1):
                   oc=oc+"00000000"+binary_convert(int(disp,16))
                   return convertF3(oc)
               elif (n==2):
                   oc=oc+"0000"+binary_convert(int(disp[0],16))+binary_convert(int(disp[1],16))
                   return convertF3(oc)
               else:
                   oc=oc+binary_convert(int(disp[0],16))+binary_convert(int(disp[1],16))+\
                   binary_convert(int(disp[2],16))
                   return convertF3(oc)
        else:
               if(check_base(add,base_add)):
                    oc=oc+"100"
                    disp=int(add,16)-int(base_add,16)
                    if disp<0:                              #check backward reference
                      disp=tohex(disp,12)
                      disp=disp[2:]
                    else:
                      disp=hex(disp)
                      disp=disp[2:]
                    n=len(disp)
                    if(n==1):
                       oc=oc+"00000000"+binary_convert(int(disp,16))
                       return convertF3(oc)
                    elif (n==2):
                       oc=oc+"0000"+binary_convert(int(disp[0],16))+binary_convert(int(disp[1],16))
                       return convertF3(oc)
                    else:
                        oc=oc+binary_convert(int(disp[0],16))+binary_convert(int(disp[1],16))+\
                   binary_convert(int(disp[2],16)) 
                        return convertF3(oc)
               else:
                    return "ERROR"
        
    else:
         if label=="-" and  add=="-":                          #RSUB - -
            oc=oc+"110000"+"000000000000"
            return convertF3(oc)
         count=0
         for i in range(len(label)):                             #index addressing mode
            if label[i]==',':
               if label[i+1]=="X":
                   oc=oc+"111"
                   count=1
                   break
         if count==1:
             if(check_PC(add,next_add)):                     #pc relative addressing
               oc=oc+"010"                                   # stch buffer,x
               disp=int(add,16)-int(next_add,16)
               if disp<0:                              #check backward reference
                  disp=tohex(disp,12)
                  disp=disp[2:]
               else:
                  disp=hex(disp)
                  disp=disp[2:]
               n=len(disp)
               if(n==1):
                   oc=oc+"00000000"+binary_convert(int(disp,16))
                   return convertF3(oc)
               elif (n==2):
                   oc=oc+"0000"+binary_convert(int(disp[0],16))+binary_convert(int(disp[1],16))
                   return convertF3(oc)
               else:
                   oc=oc+binary_convert(int(disp[0],16))+binary_convert(int(disp[1],16))+\
                   binary_convert(int(disp[2],16))
                   return convertF3(oc)
             else:
               if(check_base(add,base_add)):
                    oc=oc+"100"
                    disp=int(add,16)-int(base_add,16)
                    if disp<0:                              #check backward reference
                      disp=tohex(disp,12)
                      disp=disp[2:]
                    else:
                      disp=hex(disp)
                      disp=disp[2:]
                    n=len(disp)
                    if(n==1):
                       oc=oc+"00000000"+binary_convert(int(disp,16))
                       return convertF3(oc)
                    elif (n==2):
                       oc=oc+"0000"+binary_convert(int(disp[0],16))+binary_convert(int(disp[1],16))
                       return convertF3(oc)
                    else:
                        oc=oc+binary_convert(int(disp[0],16))+binary_convert(int(disp[1],16))+\
                   binary_convert(int(disp[2],16)) 
                        return convertF3(oc)
               else:
                    return "ERROR"
             
         if count==0:
            oc=oc+"110"                                     #direct addresssing
            if(check_PC(add,next_add)):                     #pc relative addressing
               oc=oc+"010"                                   # stch buffer,x
               disp=int(add,16)-int(next_add,16)
               if disp<0:                              #check backward reference
                  disp=tohex(disp,12)
                  disp=disp[2:]
               else:
                  disp=hex(disp)
                  disp=disp[2:]
               n=len(disp)
               if(n==1):
                   oc=oc+"00000000"+binary_convert(int(disp,16))
                   return convertF3(oc)
                   
               elif (n==2):
                   oc=oc+"0000"+binary_convert(int(disp[0],16))+binary_convert(int(disp[1],16))
                   return convertF3(oc)
               else:
                   oc=oc+binary_convert(int(disp[0],16))+binary_convert(int(disp[1],16))+\
                   binary_convert(int(disp[2],16))
                   return convertF3(oc)
            else:
               if(check_base(add,base_add)):
                    oc=oc+"100"
                    disp=int(add,16)-int(base_add,16)
                    if disp<0:                              #check backward reference
                      disp=tohex(disp,12)
                      disp=disp[2:]
                    else:
                      disp=hex(disp)
                      disp=disp[2:]
                    n=len(disp)
                    if(n==1):
                       oc=oc+"00000000"+binary_convert(int(disp,16))
                       return convertF3(oc)
                    elif (n==2):
                       oc=oc+"0000"+binary_convert(int(disp[0],16))+binary_convert(int(disp[1],16))
                       return convertF3(oc)
                    else:
                        oc=oc+binary_convert(int(disp[0],16))+binary_convert(int(disp[1],16))+\
                   binary_convert(int(disp[2],16)) 
                        return convertF3(oc)
               else:
                    return "ERROR"
            
                   
        
def convertF3(oc):
    s1=oc[:4]                                                      #convert bin to hex                                  
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
    s6=oc[20:24]
    s6=hex(int(s6,2))
    s6=s6.upper()
    s1=s1[2:]+s2[2:]+s3[2:]+s4[2:]+s5[2:]+s6[2:]
    return s1                  
          
         
           
           
    
    
def format4(op,label,add): 
    num=opcodeF3nF4[op[1:]]
    oc=binary_convert(int(num[0],16))             
    temp=binary_convert(int(num[1],16))          #opcode 2 bit only
    oc=oc+temp[:2]
    if label[0]=="#" :                           #register and address
        oc=oc+"010001"
        if (label[1:].isdigit()):
           temp=label[1:]
           temp=hex(int(temp))     #+jsub #4096 #is single enter #0001
           temp=temp[2:]                           #remove ox
           n=len(temp)
           if n==1:
               oc=oc+"0000000000000000"+binary_convert(int(temp[0],16))
           elif n==2:
               oc=oc+"000000000000"+binary_convert(int(temp[0],16))+binary_convert(int(temp[1],16))
           elif n==3:
               oc=oc+"00000000"+binary_convert(int(temp[0],16))+binary_convert(int(temp[1],16))+\
               binary_convert(int(temp[2],16))
           else:    
               oc=oc+"0000"+binary_convert(int(temp[0],16))+binary_convert(int(temp[1],16))+\
               binary_convert(int(temp[2],16))+binary_convert(int(temp[3],16))   
        else:
           oc=oc+"0000"+binary_convert(int(add[0],16))+binary_convert(int(add[1],16))+\
           binary_convert(int(add[2],16))+binary_convert(int(add[3],16))        
    elif (label=="MAXLEN"):
        oc=oc+"010001"+"00000001000000000000"
    else:
        oc=oc+"110001"+"0000"                              #+jsub #table2
        oc=oc+binary_convert(int(add[0],16))+binary_convert(int(add[1],16))+\
        binary_convert(int(add[2],16))+binary_convert(int(add[3],16))
       
    s1=oc[:4]                                                
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
    s6=oc[20:24]
    s6=hex(int(s6,2))
    s6=s6.upper()
    s7=oc[24:28]
    s7=hex(int(s7,2))
    s7=s7.upper()
    s8=oc[28:]
    s8=hex(int(s8,2))
    s8=s8.upper()
    s1=s1[2:]+s2[2:]+s3[2:]+s4[2:]+s5[2:]+s6[2:]+s7[2:]+s8[2:]
    return s1                                        #generate object code convert bin to hexa
    
 #########################################################################################   
register={"A":"0","X":"1","L":"2","P":"8","W":"9","B":"3","S":"4","T":"5","F":"6"}
opcodeF1={"FIX":"C4","FLOAT":"C0","HIO":"F4","NORM":"C8","SIO":"F0","TIO":"F8"}      #format 1 opcodes
opcodeF2={"ADDR":"90","CLEAR":"B4","COMPR":"A0","DIVR":"9C","MULR":"98","RMO":"AC",\
          "SHIFTL":"A4","SHIFTR":"A8","SUBR":"94","SVC":"B0","TIXR":"B8"}            #format 2 opcode
opcodeF3nF4={"ADD":"18","ADDF":"58","AND":"40","COMP":"28","COMPF":"88","DIV":"24",\
             "DIVF":"64","J":"3C","JEQ":"30","JGT":"34","JLT":"38","JSUB":"48",\
             "LDA":"00","LDB":"68","LDCH":"50","LDF":"70","LDL":"08","LDS":"6C","LDT":"74",\
             "LDX":"04","LPS":"D0","MUL":"20","MULF":"60","OR":"44","RD":"D8","RSUB":"4C",\
             "SSK":"EC","STA":"0C","STB":"78","STCH":"54","STF":"80","STI":"D4","STL":"14",\
             "STS":"7C","STSW":"E8","STT":"84","STX":"10","SUB":"1C","SUBF":"5C","TD":"E0",\
             "TIX":"2C","WD":"DC"}                                                  #format 3n4 opcodes
 
def call2(op,label,address,next_address,base_address):
    op=op.upper()
    label=label.upper()
    address=address.upper()
    next_address=next_address.upper()
    base_address=base_address.upper()
    try:
        if (op=="BYTE" or op=="WORD") and address=="-":#Word or byte instruction
            if label[0]=="X":                                       #BYTE X'F1'
              for i in range(len(label)):
                 if label[i]=="'":
                      return label[i+1:len(label)-1]                
            if label=="C'EOF'":                                   #EOF instruction
               return "454F46"
        elif (op=="START" or op=="BASE" or op=="END" or op=="RESW" or op=="RESB"):
           return "No object code  for such instruction" #
        elif (check_f1(op)):
           return format1(op)              #call format1
        elif (check_f2(op)):
           return format2(op,label)
        elif (check_f4(op)):
          return  format4(op,label,address)
        else:
           return format3(op,label,address,next_address,base_address)
     
    except KeyError:
      return "INVALID opcode"
    except:
      return "Oops Invalid Input"
        

                                                                   
