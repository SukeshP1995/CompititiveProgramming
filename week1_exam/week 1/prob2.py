from functools import reduce

def dfs(room, ckey, marked):

	for key in ckey:
		if not marked[key]:
			marked[key] = True
			if key < len(room):
				dfs(room, room[key], marked)

rooms = [[[1], [0,2], [3]], [[1,3], [3,0,1], [2], [0]], [[1], [0,2], [3]], [[1,3], [3,0,1], [2], [0]],  [[1,2,3], [0], [0], [0]] , [[1], [0,2,4], [1,3,4], [2], [1,2]], [[1], [2,3], [1,2], [4], [1], [5]], [[1], [2], [3], [4], [2]] , [[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]] ]

for room in rooms:
	print(room)
	N = 0
	for keys in room:
		if keys:
			tmax = max(keys)
			if tmax > N:
				N = tmax

	
	marked = [True] + [False]*N
	dfs(room, room[0], marked)

	print(marked)
	print(reduce(lambda x, y: (x and y), marked))