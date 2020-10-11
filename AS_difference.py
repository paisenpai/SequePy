def Init():
    while True:
        total = 0
        tn = 0
        value = []
        while True:
            try:
                a = float(input("Please enter the first number of the sequence. \n"))
                an = float(input("Please enter the last number of the sequence.\n"))
                n = int(input("Please enter the length of the sequence. \n"))
                assert n > 1
                break
            except:
                print("Invalid Character")
        
        
        print("\nResults:")
        total = n * ((a + an) / 2)
        d = (an - a)/(n - 1)
        print('The common difference of the sequence =', d)
        print('The sum of the arithmetic sequence =', total)
        
        closer = str(input("\nEnter 1 to exit.\nPress any key to continue.\n"))
        if(closer == '1'):
            return
            
                