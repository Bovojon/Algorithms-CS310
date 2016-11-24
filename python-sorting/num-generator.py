import random

def number_generator(n):
	listNums = []
	for i in range(n):
		a = random.randint(0,1000)
		listNums.append(a)

	f = open('{}.txt'.format(n), 'w')
	f.write(str(listNums)[1:-1])
	f.close()

	print(str(listNums)[1:-1])



number_generator(1000);
