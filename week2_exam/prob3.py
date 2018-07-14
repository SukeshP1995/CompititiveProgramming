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










for grid in grids:
	
	h = []
	v = []
	print(grid)
	for r in range(len(grid)):
		for c in range(len(grid[r])):
			if grid[r][c]==1:
				h.append(r)
				v.append(c)
	v.sort()
	h.sort()
	# print(v, h)

	m = len(v)//2
	dist = 0
	if v and h:
		x = h[m]
		y = v[m]

		for r in range(len(grid)):
			for c in range(len(grid[r])):
				if grid[r][c]==1:
					dist += abs(x-r) + abs(y-c)
	print(dist)