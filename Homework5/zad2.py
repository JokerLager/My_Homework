import random
player_one = {'счет': 1000}
player_two = {'счет': 1000}
first = input(""""Приветствую вас в казино Пери 777.У вас 1000 биткоинов.
Только мы заботимся о вас и ваших деньгах поэтому мы не забираем процент от вашей выигранной ставки.
У нас вы можете поиграть в:
1.Black Jack.
2.Казино.
3.Игровые автоматы. """ )
if first == 1:
	print("""Приветствую вас в игре black jack.Правила игры совершенно просты.Каждому игроку раздаются две карты.
У кого сумма карт больше приближены к 21 тот и выиграл.""")

	name = input('Имя первого игрока: ')
	name2 = input('Имя второго игрока: ')
	while True:
		name['ставка'] = int(input("Первый игрок ставит: "))
		name2['ставка'] = int(input("Второй игрок ставит: "))
		if name["ставка"] != name2["ставка"]
			while True:
				name['ставка'] = int(input("Уравняйте ставки"))
				name2['ставка'] = int(input("Уравняйте ставки")
				if name["ставка"] == name2["ставка"]:
					print("Ставки уравнены")
					brea	
	name['бросок'] = random.randint(1, 11)	
	name2['бросок'] = random.randint(1, 11)

	print('У первого игрока выпало ', player_one['бросок'], 'очков')
	print('У второго игрока выпало ', player_two['бросок'], 'очков')

	if player_one['бросок'] > player_two['бросок']:
		print("Первый игрок выиграл ставку")
		player_one['счет'] += player_two['ставка']
		player_two['счет'] -= player_two['ставка']	
	elif player_one['бросок'] < player_two['бросок']:
		print("Второй игрок выиграл ставку")
		player_two['счет'] += player_one['ставка']
		player_one['счет'] -= player_one['ставка']
	else:
		print("Ничья")

	print("У первого игрока на счету ", player_one['счет'])
	print("У второго игрока на счету ", player_two['счет'])

	if player_one['счет'] <= 0:
		print('Первый игрок обанкротился. Второй игрок выиграл')
		break
	if player_two['счет'] <= 0:
		print('Второй игрок обанкротился. Первый игрок выиграл')
		break