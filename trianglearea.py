def Init():
	while True:
		try:
			base = int(input("input the base length of the triangle: "))
			height = int(input("input the height of the triangle: "))

			area = (height * base) / 2

			print('\nthe area of the triangle is: %s\n' % area)
		except:
			print("That's not a valid number")


