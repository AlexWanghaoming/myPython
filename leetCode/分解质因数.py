def s(num: int):
	if num == 1:
		return num
	while num != 1:
		for i in range(2, num+1):
			if num % i ==0:
				num //= i
				if num == 1:
					print(i)
				else:
					print(str(i) + "*", end="")
				break

s(90)

