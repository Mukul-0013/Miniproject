''' Miniproject Code on Random Password Generator '''
import string
from tkinter import *
from tkinter import Tk
import os
from time import time
import pyperclip

# Global variable for storing Password
randPass=""

# For Generating random number
def rand_num(x,y):
   sub=y-x
   z=int(time() - float(str(time()).split('.')[0]))
   random=int((time() - float(str(time()).split('.')[0]))*(10**16))
   random %=sub
   random+=x
   return random

# For Generating time in some fractions seconds
def rand_val():
   random=float((time() - float(str(time()).split('.')[0]))*(0.001))
   return random

# For Generating random character according to ASCII code
def rand_char(x,y):
   sub=y-x
   z=int(time() - float(str(time()).split('.')[0]))
   random=int((time() - float(str(time()).split('.')[0]))*(10**16))
   random %=sub
   random+=x
   return chr(random)

# For Generating random element
def rand_element(element):
    a=rand_num(1,11)
    if element==1:
        x=rand_char(33,48)
    elif element==2:
        x=rand_char(65,91)
    elif element==3:
        x=rand_num(1,10)
    elif element==4:
        x=rand_char(97,123)
    elif element==5:
        x=rand_char(33,48)
    elif a==1:
        x=rand_char(65,91)
    elif a==2:
        x=rand_char(97,123)
    elif a==3:
        x=rand_char(33,48)
    elif a==4:
        x=rand_num(1,10)
    elif a==5:
        x=rand_char(33,127)
    elif a==6:
        x=rand_num(1,10)
    elif a==7:
        x=rand_char(58,65)
    elif a==8:
        x=rand_char(65,91)
    elif a==9:
        x=rand_char(91,97)
    elif a==10:
        x=rand_char(97,123)
    return x

def listToString(arr):
    str = ""
    for element in arr:
        str += element
    return str

def click():
    password = generatePassword()
    output.delete(0.0, END)
    global randPass
    try:
        randPass = listToString(password)
    except:
        randPass = "There is somethong wrong :("
    output.insert(END, randPass)

def clear():
    output.delete(0.0, END)

def generatePassword():

    length = rand_num(12,33)
    password = [length]
    for element in range(length):
        import time
        time.sleep(rand_val())
        password.append(str(rand_element(element)))

    length = len(password)

    # Make first char small letter
    password[0] = rand_char(97,123)
    # time lapse for some fractions of seconds for randomization
    import time
    time.sleep(rand_val())
    # Make last char capital letter
    password[length - 1] = rand_char(65,91)

    return password

#Command to copy the password on clipboard
def copyToClipboard():
    pyperclip.copy(randPass)

if __name__ == "__main__":

    rpg = Tk()
    rpg.geometry("500x200")
    rpg.title("Random Password Generator")

    Label(rpg, text="Click to generate a new random password:", font="calibri 20 bold").pack(pady=3)

    Button(rpg, text="Generate", width=8, command=click).pack(pady=7)

    output = Text(rpg, width=40, height=1, wrap=WORD, background="white")
    output.pack(pady=3)

    Button(rpg, text="Copy to clipboard", width=17, command=copyToClipboard).pack(pady=7)

    Button(rpg, text="CLEAR", width=5, command=clear).pack(pady=7)

    rpg.mainloop()
