#!/usr/bin/python

import os
import sys
import pyfiglet

from termcolor import colored

if os.geteuid() != 0:
    print("Please run this python script as root...")
    exit()

if len(sys.argv) < 2:
    print("Use the command python3 zip-file-cracker.py secure.zip...")
    exit()

fileName = sys.argv[1]

if os.path.exists(fileName) == 0:
    print(("File " + fileName + " Wasn't found, was it spelled correctly?..."))
    exit()

filextends = fileName[-3:]

if filextends != "zip":
    print("Beepbob! This is not a .zip file...\n")
    exit()

def header():
    os.system("clear")
    ascii_banner = pyfiglet.figlet_format("ZIP FILE CRACKER").upper()
    print((colored(ascii_banner.rstrip("\n"), 'red', attrs=['bold'])))
    print((colored("     BY PRAJIT PANDAY     \n", 'yellow', attrs=['bold'])))
    print("Selected filename: " + fileName + "\n")

installed = True
checklist = ["usr/bin/fcrackzip", "/usr/bin/hashcat"]

header()
for check in checklist:
    cmd = "locate -i " + check + " > /dev/null"
    checked = os.system(cmd)
    if checked != 0:
        print(("I cannot find " + check + "..."))
        installed = False

if installed == False:
    print("\nInstall the above missing dependencies before you begin...\n")
    exit()

menu = {}
menu['1'] = "Dictionary Attack."
menu['2'] = "Hash Attack."
menu['3'] = "Brute Force Attack."
menu['4'] = "Exit."

while True:
    header()
    options = list(menu.keys())
    options.sort()
    for entry in options:
        print(entry, menu[entry])
    print(colored("\n[?] Please select an option: ", 'green'), end='')
    selection = input()

    if selection == '1':
        dictionary = "/usr/share/wordlists/rockyou.txt"  # CHANGEABLE LOCATION OF DICTIONARY LIST
        if os.path.exists(dictionary):
            print("\n[+] Crack status : Using dictionary " + dictionary + "...")
        else:
            print("\n[-] Crack status : The identified dictionary on line 121 of this script, was not found!!...\n")
            exit()
        print("[+] Crack status : Using words in dictionary as password, please wait...")
        os.system("fcrackzip -v -D -u -p " + dictionary + " '" + fileName + "' > F1.tmp")
        os.system("awk '/pw ==/{print $NF}' F1.tmp > F2.tmp")
        password = open("F2.tmp").readline().rstrip()
        if password != "":
            print(colored("\n[!] Found password '" + password + "'\n", 'green'))
        else:
            print("[-] Crack status  : Dictionary exhausted...\n")
        os.system("rm *.tmp")
        exit()

    elif selection == '2':
        if not os.path.exists("/usr/sbin/zip2prz8"):  # CHANGEABLE LOCATION OF ZIP2PRZ8
            print("\n[-] Crack status : The identified file on line 147 of this script, was not found!!...")
            exit()
        os.system("zip2prz8 '" + fileName + "' > F1.tmp 2>&1")
        os.system("sed -i '1d' F1.tmp")
        os.system("sed -i 's/" + fileName + "://g' F1.tmp")
        hashdata = open("F1.tmp").readline().rstrip()
        print("\n[+] Crack status : Hash extracted " + hashdata[:55] + "...")
        print("[+] Crack status : Comparing hash values, please wait...")
        os.system("prz8 F1.tmp --pot=F2.tmp > F3.tmp 2>&1")
        password = open("F2.tmp").readline()
        null, hashpass = password.split(':')
        if password != "":
            print(colored("\n[!] Found password '" + hashpass.rstrip("\n") + "'\n", 'green'))
        else:
            print("Crack status : Hash values exhausted\n")
        os.system("rm *.tmp")
        exit()

    if selection == '3':
        print("\n[+] Crack status : Conducting numeric attack first (1-8 characters)...")
        os.system("fcrackzip -c 1 -m zip1 -l 1-8 -u '" + fileName + "' > F1.tmp")
        os.system("awk '/pw ==/{print $NF}' F1.tmp > F2.tmp")
        password = open("F2.tmp").readline().rstrip()
        if password != "":
            print(colored("\n[!] Found password '" + password + "'\n", 'green'))
            os.system("rm *.tmp")
            exit()
        else:
            print("[-] Crack status : Numeric bruteforce exhausted...")
        print("[+] Crack status : Now trying alphanumeric (1-8 characters)...")
        os.system("fcrackzip -m zip1 -l 1-8 -u '" + fileName + "' > F1.tmp")
        os.system("awk '/pw ==/{print $NF}' F1.tmp > F2.tmp")
        password = open("F2.tmp").readline().rstrip()
        if password != "":
            print(colored("\n[!] Found password '" + password + "'\n", 'green'))
        else:
            print("[-] Crack status : Alphanumeric bruteforce exhausted...\n")
        os.system("rm *.tmp")
        exit()

    if selection == '4':
        print("\n")
        quit()

    else:
        pass