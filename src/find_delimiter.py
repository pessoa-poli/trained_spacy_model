import re;

phrase = ("With a smart thermostat, you can easily control the temperature of your home from anywhere using your smartphone or tablet.", 7, 22, "device")

pattern = 'smart thermostat'
matches = re.search("smart thermostat", phrase[0],  re.IGNORECASE)
print('The result of the search is: ')
print(matches)
print()