def sum():
	sum = 0
	a = 1
	b = 2
	while (b < 4000000):
		if b % 2 == 0:
			sum += b
		b = a + b
		a = b - a
	return sum
print(sum())
