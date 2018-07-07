str1, str2 = input().split(', ')
str1 = ''.join(sorted(list(str1.lower()))).strip()
str2 = ''.join(sorted(list(str2.lower()))).strip()
if str1 == str2:
	print(True)
else:
	print(False)