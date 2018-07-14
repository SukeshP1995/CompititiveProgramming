x = int(input('x : '))
y = int(input('y : '))

z = x ^ y

n = 0
while z:
	if z & 1:
		n += 1
	z >>= 1
print(n)