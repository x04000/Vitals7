import time
import os
import sys
from getpass import getpass

# \\\ Vitals 7 Sistem Configs ///

# Vitals 7 - Host
v7host = "@AnOtherShadow"

# Vitals 7 - User Credentials
user = "Admin"
password = "1234"

# Vitals 7 - Root Credentials
rootusr = "root"

# Vitals 7 - Color
v7color = "\x1b[0;35m"

# Vitals 7 - Terminal
v7usr = user
v7info = "\x1b[38;2;0;255;116m[\x1b[0;36m!\x1b[38;2;0;255;116m] "
v7info = "\n\x1b[38;2;0;255;116m[\x1b[0;36m!\x1b[38;2;0;255;116m] "
v7warning = "\x1b[38;2;255;100;0m[\x1b[0;36m!\x1b[38;2;255;100;0m] "
v7warningi = "\n\x1b[38;2;255;100;0m[\x1b[0;36m!\x1b[38;2;255;100;0m] "
v7error = "\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] "
v7errori = "\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] "
v7terminalcolor1 = "\x1b[38;2;0;255;251m"
v7terminalcolor2 = "\x1b[0;35m"
v7terminalcolor3 = "\x1b[38;2;255;0;0m"
v7ti = f'{v7terminalcolor1}{v7usr}{v7terminalcolor2}@{v7terminalcolor3}{v7host}{v7terminalcolor1}❯ {v7color}'

# Vitals 7 - Distro Info
distro = "Orignal"
author = "x04000"
def v7logo():
    print("""

 ██▒   █▓ ██▓▄▄▄█████▓ ▄▄▄       ██▓      ██████    ███████╗
▓██░   █▒▓██▒▓  ██▒ ▓▒▒████▄    ▓██▒    ▒██    ▒    ╚════██║
 ▓██  █▒░▒██▒▒ ▓██░ ▒░▒██  ▀█▄  ▒██░    ░ ▓██▄          ██╔╝
  ▒██ █░░░██░░ ▓██▓ ░ ░██▄▄▄▄██ ▒██░      ▒   ██▒      ██╔╝
   ▒▀█░  ░██░  ▒██▒ ░  ▓█   ▓██▒░██████▒▒██████▒▒     ██╔╝ 
   ░ ▐░  ░▓    ▒ ░░    ▒▒   ▓▒█░░ ▒░▓  ░▒ ▒▓▒ ▒ ░     ╚═╝ 
   ░ ░░   ▒ ░    ░      ▒   ▒▒ ░░ ░ ▒  ░░ ░▒  ░ ░   
     ░░   ▒ ░  ░        ░   ▒     ░ ░   ░  ░  ░     
      ░   ░                 ░  ░    ░  ░      ░     
     ░       
    """)
    print("| Distro: "+distro)
    print("| by "+author)

# Vitals 7 - Load Times
updaterloadtime1 = 1.5
updaterloadtime2 = 1
updaterloadtime3 = 0.5
updaterloadtime4 = 2

# Vitals 7 - Functions
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
def v7progressbar():
    print("[          ]", end='\r')
    time.sleep(0.1)
    print("[■         ]", end='\r')
    time.sleep(0.2)
    print("[■■        ]", end='\r')
    time.sleep(0.4)
    print("[■■■       ]", end='\r')
    time.sleep(0.2)
    print("[■■■■      ]", end='\r')
    time.sleep(0.1)
    print("[■■■■■     ]", end='\r')
    time.sleep(0.5)
    print("[■■■■■■    ]", end='\r')
    time.sleep(0.1)
    print("[■■■■■■■   ]", end='\r')
    time.sleep(0.3)
    print("[■■■■■■■■  ]", end='\r')
    time.sleep(0.2)
    print("[■■■■■■■■■ ]", end='\r')
    time.sleep(0.2)
    print("[■■■■■■■■■■]", end='\r')
    time.sleep(0.5)
def v7progressbar2():
    for i in enumerate(list(range(10))):
        print("|           ", end='\r')
        time.sleep(0.1)
        print("/           ", end='\r')
        time.sleep(0.1)
        print("-           ", end='\r')
        time.sleep(0.1)
        print("\\           ", end='\r')
        time.sleep(0.1)
    print("Done!", end='\r')

def v7clear():
    try:
        os.system("clear")
    except:
        print("")

# Vitals 7 - Updater
def v7updater():
    slowprint("Checking updates...")
    print("The system goes to download a file from github to verify your version")
    print("File: https://raw.githubusercontent.com/x04000/Vitals7/main/vitals7/version")
    time.sleep(updaterloadtime1)
    try:
        os.system("wget https://raw.githubusercontent.com/x04000/Vitals7/main/vitals7/version")
        with open("version","r") as file:
                for line in file:
                    lastestversion = line
        with open("vitals7/version","r") as file1:
                for line1 in file1:
                    currentversion = line1
        os.system("rm version")
        time.sleep(updaterloadtime2)
        v7clear()
        v7logo()
        if currentversion < lastestversion:
            print(v7warning+"Vitals 7 is not updated!")
            print(v7warning+"You version is "+currentversion+v7warning+"The lastest version is "+lastestversion+"!")
            print("")
            print("Do you want to update Vitals 7? [Y/n]")
            v7t = str(input(v7ti))
            if v7t == "Y" or v7t == "y":
                try:
                    os.system("python3 vitals7/Vitals7Updater.py")
                except:
                    print(v7errori+"Keyboard interrupt")
            elif v7t == "N" or v7t == "n":
                slowprint(v7info+"Skipped Vitals 7 Updater")
                time.sleep(updaterloadtime3)
            else:
                slowprint("\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Invalid option")
                time.sleep(updaterloadtime3)
        else:
            print(v7info+"Vitals 7 is updated :)")
            print(v7info+"You version is "+currentversion+v7info+"The lastest version is "+lastestversion)
            time.sleep(updaterloadtime4)
    except KeyboardInterrupt:
        print(v7errori+"Keyboard Interrupt")
    except:
        print(v7errori+"A error ocurred during module installation!")
        exit()