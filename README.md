# Object-Code-Generator

Object Code is the output of an assembler after it processes source code. Both SIC and SIC/XE assembler basically uses two algorithms to generate the object code namely Pass 1(to define symbols) and Pass 2(to generate object code).The Object Code Generator is a partial implementation of Pass 2. User has to provide a single SIC or SIC/XE instruction for which the object code has to be generated. For SIC instruction the user has to provide three inputs i.e. Mnemonic opcode, operand, operand address and for the SIC/XE instruction the user has to providefive inputs i.e. Mnemonic opcode, operand, operand address, PC(next instruction address), base address. The Object Code generator will provide an User Interface to select the instruction type and enter the inputs.
 
## About this repository

This repository contains the code for Object Code generator which has the capability to generate Object Code for SIC or SIC/XE instructions. 

## Requirements
Programming Language - Python 3.6                                                                                                                                                                           
Modules - Tkinter  ( You don’t need to worry about installation of the Tkinter module as it comes with Python default)

## Screenshots

![ogc](https://user-images.githubusercontent.com/73954439/98199152-930ed680-1f50-11eb-8972-b9d25c36034b.png)

Main Window has 2 buttons to select the instruction type i.e. SIC button and SIC/XE button.

![SIC_window](https://user-images.githubusercontent.com/73954439/98194111-a9af3080-1f44-11eb-8830-8efb6f77298b.png)

SIC Window has three input fields i.e. Mnemonic opcode , Operand, Operand
Address and a text label to display the output. There are two buttons, Generate
(generate opcode) and Clear (clear the input fields ).

![SICXE_window](https://user-images.githubusercontent.com/73954439/98194897-72da1a00-1f46-11eb-8cdd-21410b5ec94e.png)

SIC/XE Window has five input fields i.e. Mnemonic opcode,Operand,Operand
Address,PC Address, Base Address and a text label to display the output. There are
two buttons,Generate(generate opcode) and Clear(clear the input fields ).

![g5](https://user-images.githubusercontent.com/73954439/98194958-a0bf5e80-1f46-11eb-9dfa-e34fca3bf750.png)

SIC instruction result


![s8](https://user-images.githubusercontent.com/73954439/98195011-c187b400-1f46-11eb-8a62-fec0a31b18de.png)

SIC/XE result.
