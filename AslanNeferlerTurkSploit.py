
import os
import re

os.system("clear")
#Colors 
red = '\033[91m'
green = '\033[92m'
white = '\033[97m'
dgreen = '\033[32m'
yellow = '\033[93m'
back = '\033[7;91m'
blink = '\033[5m'
light_blue = '\033[1;34m'

print ('''\033[93m༄༄༄༄༄༄༄༄༄༄༄༄
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄AslanNeferler Turksploit ༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄%sby KeuTurHan  ヅ\033[0m\n''' % red)

print("\033[32m işlemi başlatmak için TurkSploit yazın" )

veri = input("İşlem:")

if veri =="TurkSploit":
 x =input(" '\033[91mMetasploit kurulumu için Entere basın")
 os.chdir("/data/data/com.termux/files/home/")
 os.system("pkg update && pkg upgrade -y &&pkg install postgresql && pkg install openssh wget curl git -y && wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh && chmod +x  metasploit.sh && ./metasploit.sh")
 os.system("msfconsole")