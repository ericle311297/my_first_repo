def largestPrimeFactor():
	num = 600851475143
	index = 2
	while index*index < num:
		while num % index == 0:
			num = num / index
		index = index + 1
	return num

print(largestPrimeFactor())
