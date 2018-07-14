def quantity(lst):





lst = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

start = 0
end = 1
buff = 0
for i in range(1, len(lst)):
	if lst[i] < lst[i-1]:
		buff += 1
	