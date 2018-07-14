def paranComb(res, lst, openp, indp, closep, n):
	# print(lst)
	if closep == n:
		res.append(''.join(lst))
	else:
		if openp > closep:
			lst[indp] = ')'
			paranComb(res, lst, openp, indp+1, closep+1, n)
		if openp < n:
			lst[indp] = '('
			paranComb(res, lst, openp+1, indp+1, closep, n)

n = int(input())
res = []
paranComb(res, ['']*2*n, 0, 0, 0, n)
print(res)
print(len(res))