while True:
	name = input("""Как тебя зовут ?
""")
	math = float(input('Какие у тебя оценки по математике? '))
	fizika = float(input("Какие у тебя оценки по физике? "))
	himiya = float(input("Какие у тебя оценки по химии? "))
	biology = float(input("Какие у тебя оценки по биологии? "))
	geografy = float(input("Какие у тебя оценки по географии? "))
	n = (math + fizika + himiya + biology + geografy) / 5
	if n >= 4.8:
		print("Поздравляем тебя ты прошел.У тебя" , n , "баллов")
		break
	else:
		print("Ты не подходишь.У тебя" , n , "баллов")
		continue 	