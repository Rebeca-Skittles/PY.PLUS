# (C)2022 XER+
# Version: 1.0.0

# IMPORTS

# REGESTREY
onsrt = 1
onsrte = 69
key = 85252859850285289858298329582583282904825259889440

# VARIABLES
h = "CMD1: 1 CMD2: ?plus1 CMD3: cmdr "
cmdinput = ""

# ON START
def start():
    if onsrt < onsrte:
       print("Welcome To PY.PLUS")
       print("Type 'Help' For a List Of Commands")
       print("To Exit use CTRL + C")
    elif onsrte == 2:
       print("Error 004: INVAL_ONSRTE")

start()

# LIST SYSTEM

# list1
ply12 = ["Simple Text", "COMMAND_LIST: ply12", "COMMAND_FUN: plus1"]
# list1 END

# END OF LIST SYSTEM

# FUNCTIONS

# plus1
def plus1():
      print(ply12[0])
# plus1 END
# ?plus1
def abp1():
     print(ply12[1])
     print(ply12[2])
# ?plus1 END
# help
def h():
    print(h)
# help END

# END OF FUNCTIONS

# ERROR 001 & 002
if onsrt > onsrte:
       print("Error 001: INVAL_REGY.PLUS")
elif onsrt == onsrte:
       print("Error 002: Regersty does not have the correct setings for PY.PLUS to work")

# ERROR 003
if key == onsrte:
       print("Error 003: Invalid Key Usage")
elif key == onsrt:
       print("Error 003: Invalid Key Usage")

# REPEAT SYSTEM
while True:
    cmdinput = input()

    # CMDINPUT
    if cmdinput == "1":
        plus1()
    if cmdinput == "?plus1":
        abp1()
    if cmdinput == "cmdr":
        start()
    if cmdinput == "help":
        h()
# PY.PLUS END