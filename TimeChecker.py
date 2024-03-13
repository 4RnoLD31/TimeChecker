# -*- coding: utf-8 -*-
import configparser
import os
import time
import datetime

def cls():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def set_time():
	print("Set time. Ex: 14:50, 03:34. Or use empty string to set current time")
	time = input(">>> ")
	if time == "":
		time = datetime.datetime.now().strftime("%H:%M")
	print("Set date. Ex: 13.03.2024, 01.03.2024. Or use empty string to set current date")
	date = input(">>> ")
	if date == "":
		date = datetime.datetime.now().strftime("%d.%m.%Y")
	print(f"Done. {time + ' ' + date}")
	return time + " " + date

def during(first, second):
	first_day = int(first[6:8])
	first_hours = int(first[:2])
	first_minutes = int(first[3:5])
	second_day = int(second[6:8])
	second_hours = int(second[:2])
	second_minutes = int(second[3:5])
	first = datetime.timedelta(days=first_day, hours=first_hours, minutes=first_minutes)
	second = datetime.timedelta(days=second_day, hours=second_hours, minutes=second_minutes)
	return first - second

def start_activity(type_of):
	start_time = set_time()
	config[current + 1] = {
		"Type": type_of,
		"Start_time": start_time,
		"End_time": ""}
	with open("settings.ini", "w") as configfile:
		config.write(configfile)
	time.sleep(2)
	main()

def statistic():
	cls()
	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	is_first = True
	if os.stat("settings.ini").st_size == 0:
		print("There isn't any statistic yet!")
		time.sleep(2)
		main()
	for element in range(0, current + 1):
		current_time = config[str(element)]["Start_time"][6:8]
		if config[str(element)]["Start_time"][9] == "0":
			current_month = months[int(config[str(element)]["Start_time"][10]) - 1]
		else:
			current_month = months[int(config[str(element)]["Start_time"][9:11]) - 1]
		try:
			next_time = config[str(element + 1)]["Start_time"][6:8]
			if config[str(element + 1)]["Start_time"][9] == "0":
				next_month = months[int(config[str(element + 1)]["Start_time"][10]) - 1]
			else:
				next_month = months[int(config[str(element + 1)]["Start_time"][9:11]) - 1]
		except:
			next_month = current_month
			next_time = current_time
		if is_first or f"{current_month}{current_time}" != f"{next_month}{next_time}":
			print(f'{config[str(element)]["Start_time"][6:8]} {current_month}: ')
			if is_first:
				print("   ---------------------------------------------------")
			is_first = False
		print(f'  |   {config[str(element)]["Type"]}')
		print(f'  |     Start time - {config[str(element)]["Start_time"][0:5]}')
		print(f'  |     End time - {config[str(element)]["End_time"][0:5]}')
		print(f'  |     During - {during(config[str(element)]["End_time"], config[str(element)]["Start_time"])}')
		print("   ---------------------------------------------------")
	print("Press any key to return to the main menu: ")
	input(">>> ")
	main()
	

def main():
	global current, config
	types = ["OGE", "School", "Programming", "Sleeping"]
	try:
		os.stat("settings.ini").st_size
	except:
		file = open("settings.ini", "w")
		file.write("")
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
	if os.stat("settings.ini").st_size == 0:
		current = -1
	if os.stat("settings.ini").st_size == 0 or config[str(current)]["End_time"] != "":
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
