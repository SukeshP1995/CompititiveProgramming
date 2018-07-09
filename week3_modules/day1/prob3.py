import random


def rand5():
    return random.randint(1, 5)


def rand7():

    # Implement rand7() using rand5()
    rand = (rand5() - 1)*5 + rand5()

    return( rand%7 + 1 ) if rand <= 21 else rand7()


# print('Rolling 7-sided die...')
# print(rand7())

lst = [0] * 7

for i in range(1000000):
	lst[rand7()-1] += 1

print(lst)