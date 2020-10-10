def Init():
	while True:
		while True:
			try:
				n = int(input("Please enter the length of the fibonacci sequence. \n"))
				assert n > 0
				break
			except:
				print("Invalid Character")
		
		value = []
		total = 0
		
		for i in range(n):
			if i == 0 or i == 1:
				value.append(i)
			else:
				value.append(value[i - 1] + value[i - 2])
		
		print("\nResults:")
		for i in range(len(value)):
			print(i, " | ", value[i])
			total = total + value[i]
		print('The sum of the fibonacci sequence =', total)
		tn = value[-1]
		print('The nth term of the fibonacci sequence =', tn)
        
		closer = str(input("\nEnter 1 to exit.\nPress any key to continue.\n"))
		if(closer == '1'):
			return
        
				
