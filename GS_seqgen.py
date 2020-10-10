from math import pow

def Init():
    while True:
        while True:
            try:
                a = float(input("Please enter the first number of the geometric sequence. \n"))
                n = int(input("Please enter the total numbers in the geometric sequence. \n"))
                assert n > 0
                r = float(input("Please enter the common ratio.\n"))
                break
            except:
                print("Invalid Character")

        value = []
        err = False
        try:
            if r == 1:
            	total = r * n
            else:
            	total = a * (pow(r, n) - 1) / (r - 1)
            tn = a * pow(r, n - 1)
        except OverflowError:
        	print("Unable to get because of number size limits")
        	print("Use A", n, " = ", a, ' * ', r, '^', n-1, sep='')
        	print("Use S", n, " = ", a, ' * (', r, '^', n, " -1) / (", r, " - 1)", sep='')
        	err = True
        
        if err == False:
            for i in range(n):
                value.append(a * pow(r, i))

            print("\nResults:")
        
            for i in range(len(value)):
                print(i + 1, " | ", value[i])
            
            print('The sum of the geometric sequence =', total)
            print('The nth term of the geometic sequence =', tn)
            

        closer = str(input("\nEnter 1 to exit.\nPress any key to continue.\n"))
        if(closer == '1'):
            return
            