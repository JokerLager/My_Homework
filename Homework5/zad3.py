n = int(input("Введите число , факториал кторого хотите узнать."))
x = n - 1
b = x * n
n = n - 2
while True:
	b = b * n
	n = n - 1
	if n == 1:
		print(b)		
		break