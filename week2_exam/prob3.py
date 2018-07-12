grids = [[[1, 0, 0, 0, 1], 
   		[0, 0, 0, 0, 0],
   		[0, 0, 1, 0, 0]],
		[[1, 0, 1, 0, 1],
		[0, 1, 0, 0, 0], 
		[0, 1, 1, 0, 0]],
		[[1, 1],
         [1,1]],
         [[0, 0],
         [0, 0]],
         [[1, 0],
         [0, 0]]]






v = []
h = []



for grid in grids:

	print(grid)
	for r in range(len(grid)):
		for c in range(len(grid[r])):
			if grid[r][c]==1:
				h.append(r)
				v.append(c)
	v.sort()
	h.sort()


	m = len(v)//2

	x = h[m]
	y = v[m]

	dist = 0
	for r in range(len(grid)):
		for c in range(len(grid[r])):
			if grid[r][c]==1:
				dist += abs(x-r) + abs(y-c)
	print(dist)