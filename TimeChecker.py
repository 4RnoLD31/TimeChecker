import configparser
from datetime import datetime

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

def main():
	global current, config
	types = ["MSE", "School", "Programming", "Sleeping"]
	config = configparser.ConfigParser()
	config.read("settings.ini")
	index = 0
	try:
		while True:
			config[str(index)]["Type"]
			current = index
			index += 1
	except:
		pass
	if config[str(current)]["End_time"] != "":
		print("Choose the activity type: ")
		index = 1
		for element in types:
			print(f"[{index}] - {element}")
			index+=1
		choose = int(input(">>> "))
		start_activity(types[choose - 1])
	else:
		print(f'Your last activity "{config[str(current)]["Type"]} - {config[str(current)]["Start_time"]}" is not end. Do you want to add End time? [Y/N]')
		choose = input(">>> ")
		if choose == "Y":
			end_time = set_time()
			config[str(current)]["End_time"] = end_time
			with open("settings.ini", "w") as configfile:
				config.write(configfile)
		else:
			quit(0)
main()
