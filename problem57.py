def series(n):
	x = 1.0/2.0
	while n > 1:
		x = 1.0/(2.0+x)
		n = n - 1
	return 1 + x


print series(1).as_integer_ratio()
print series(2).as_integer_ratio()
print series(3).as_integer_ratio()
print series(4).as_integer_ratio()
print series(5).as_integer_ratio()