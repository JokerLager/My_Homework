m = int(input("""Сколько часов в день ты работаешь
"""))
n = m * 60
i = 0
while True:
	i = i + 1
	n += 5  
	if n  == 18 * 60:
		print("Ты прожил" , 20 + i / 12 , "Года" )
		break