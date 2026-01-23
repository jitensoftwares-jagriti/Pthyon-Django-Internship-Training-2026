janam = 1
moksha = 100

sat_karma = 5

while janam <= moksha:
	print("Janam: ", janam)
	if sat_karma > 0: # sat_karma = 5 - true
		janam += 9 # janam = 1, janam = 1 + 9 = 10
	else:
		janam += 1
		
print("Moksha achieved! 🕉️")