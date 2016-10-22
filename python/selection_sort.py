def selectionSort(numberlist):
	# Start at end of list and decrement down to start
	for i in range(len(numberlist)-1, 0,-1):
		postitionOfMax = 0
		for location in range(1,i+1):
			if numberlist[location]>numberlist[postitionOfMax]:
				postitionOfMax = location
		temp = numberlist[i]
		numberlist[i] = numberlist[postitionOfMax]
		numberlist[postitionOfMax] = temp

numberlist = [73,45,32,14,26,87,25,44,99]
selectionSort(numberlist)
print(numberlist)