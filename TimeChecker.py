# -*- coding: utf-8 -*-
import configparser
import os
import time
from datetime import datetime

def cls():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def set_time():
	print("Set time. Ex: 14:50, 03:34. Or use empty string to set current time")
	time = input(">>> ")
	if time == "":
		time = datetime.now().strftime("%H:%M")
	time = time + " " + datetime.now().strftime("%d.%m.%Y")
	print(f"Time's {time}")
	return time


def start_activity(type_of):
	start_time = set_time()
	config[current + 1] = {
		"Type": type_of,
		"Start_time": start_time,
		"End_time": ""}
	with open("settings.ini", "w") as configfile:
		config.write(configfile)
	quit(0)

def statistic():
	cls()
	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	for element in range(0, current + 1):
		if config[str(element)]["Start_time"][9] == "0":
			current_month = months[int(config[str(element)]["Start_time"][10]) - 1]
		else:
			current_month = months[int(config[str(element)]["Start_time"][9:11]) - 1]
		try:
			if config[str(element + 1)]["Start_time"][9] == "0":
				next_month = months[int(config[str(element + 1)]["Start_time"][10]) - 1]
			else:
				next_month = months[int(config[str(element + 1)]["Start_time"][9:11]) - 1]
		except:
			next_month = current_month
		print(f'{config[str(element)]["Start_time"][6:8]} {current_month}: ')
		print(f'    Type - {config[str(element)]["Type"]}')
		print(f'    Start time - {config[str(element)]["Start_time"][0:5]}')
		if config[str(element)]["Start_time"][9:11] == config[str(element)]["End_time"][9:11]:
			print(f'    End time - {config[str(element)]["Start_time"][0:5]}')
		else:
			print(f'    End time - {config[str(element)]["Start_time"]}')
	

def main():
	global current, config
	types = ["MSE", "School", "Programming", "Sleeping"]
	config = configparser.ConfigParser()
	config.read("settings.ini")
	index = 0
	cls()
	try:
		while True:
			config[str(index)]["Type"]
			current = index
			index += 1
	except:
		pass
	if config[str(current)]["End_time"] != "":
		print("Choose the activity type: ")
		print("[0] - STATISTICS")
		index = 1
		for element in types:
			print(f"[{index}] - {element}")
			index+=1
		choose = int(input(">>> "))
		if choose == 0:
			statistic()
		else:
			start_activity(types[choose - 1])
	else:
		print(f'Your last activity "{config[str(current)]["Type"]} - {config[str(current)]["Start_time"]}" is not end. Do you want to add End time? [Y/N]')
		choose = input(">>> ")
		if choose == "Y":
			end_time = set_time()
			config[str(current)]["End_time"] = end_time
			with open("settings.ini", "w") as configfile:
				config.write(configfile)
			time.sleep(2)
			main()
		else:
			quit(0)
main()
