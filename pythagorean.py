from math import sqrt
# uses pythagorean theorem
# cmath sqare root
def calcHypo(legA, legB):
	legA = float(legA)
	legB = float(legB)
	return float(sqrt((legA * legA) + (legB * legB)))
	
def calcLeg(leg, hypo):
	leg = float(leg)
	hypo = float(hypo)
	return float(sqrt((hypo * hypo) - (leg * leg)))

inLoop = True;
equationType = 0;
while True:
	while True:
		# handling error for input
		try:
			# request user input
			equationType = int(input("Press 1 to calculate"\
			" for leg\nPress 2 to calculate for hypotenuse\n"))
			if not(equationType == 1 or equationType == 2):
				# check if input is within the choices,
				# throws error if wrong input
				raise(TypeError)
			else:
				# releases while loop if success
				break
		except:
			print('Please input a valid number')
		
	inLoop = True

	if equationType == 1:
		while True:
			# handling error for input
			try:
				# request user input
				leg = float(input("Enter the length of the"\
				" other leg\n"))
				hypo = float(input("Enter the length of the"\
				" hypotenuse\n"))
				if(hypo <= leg):
					# hypotenuse is always longer in right triangles
					print("The leg shouldn't be longer than the"\
					" hypotenuse")
					raise(ValueError)
				print("\nThe length of the leg is ")
				# use defined function
				print(calcLeg(leg, hypo),'\n')
				# releases while loop if success
				break
			except:
				print("Please input a valid number")
			
	elif equationType == 2:
		while True:
			# handling error for input
			try:
				# request user input
				legA = float(input("Enter the length of the"\
				" first leg\n"))
				legB = float(input("Enter the length of the"\
				" second leg\n"))
				print("\nThe length of the hypotenuse is ")
				# use defined function
				print(calcHypo(legA, legB),'\n')
				# releases while loop if success
				break
			except:
				print("Please input a valid number")
	inLoop = True