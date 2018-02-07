import random
schet = 500
print("""Вы - игрок на криптобирже. Вас интересует курс 2-х разных криптовалют: Биткоин и Эфир.
В начале каждой недели устанавливается курс на криптовалюту.Вы должны поставить деньги ли не поставить.
У вас 500 $.Игра закончится , когда вы обанкротитесь или поднимете своё состояние до 1000 $""")
while True:
	btc = random.randint(1,1000)
	efir = random.randint(1,1000)
	print("Курс на Биткоин - ",btc)
	print("Курс на Эфир - " , efir)
	stav_btc = int(input("Сколько вы ставите на Биткоин: "))
	stav_efir = int(input("Сколько вы ставите на Эфир:"))
	btc2 = random.randint(1,1000)
	efir2 = random.randint(1,1000)
	print("Курс в конце недели на Биткоин - ",btc)
	print("Курс в конце недели на Эфир - " , efir)
	if stav_btc > 0 and btc2 > btc:
		scet = schet + stav_btc
	if stav_btc > 0 and btc2 < btc:
		scet = schet - stav_btc
	if stav_efir > 0 and efir2 > efir:
		scet = schet + stav_btc
	if stav_efir > 0 and efir2 < efir:
		scet = schet - stav_btc
	print("После перераспределения курса ваш бюджет равен:" , schet)	
	if schet <= 0 or schet >= 1000:
		print("Игра закончена")
		break