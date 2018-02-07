k = int(input("Сколько чисел Фибоначчи вывести: "))
n = 1
m = 2
print(n)
print(m)
i = 0
while True:
	i = i + 1 
	n = m + n
	print(n)
	m = n + m
	print(m)
	if i == k:
		break