import re;

phrase = ("""John appreciated how the Honeywell Home T9 Smart Thermostat provided him with detailed energy usage reports, helping him identify areas where he could save money.""", 7, 22, "device")

pattern = 'Honeywell Home T9 Smart Thermostat'
matches = re.search(pattern, phrase[0],  re.IGNORECASE)
print('The result of the search is: ')
print(matches)
print()