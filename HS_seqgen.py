def Init():
    while True:
        while True:
            try:
                a = float(input("Please enter the first number of the sequence. \n"))
                n = int(input("Please enter the length of the sequence. \n"))
                d = float(input("Please enter the common difference.\n"))
                break
            except:
                print("Invalid Character")
        
        value = []
        for i in range(n):
            value.append(a+(i)*d)
        print("\nResults:")
        for i in value:
            print('1/',i, sep='')
        
        closer = str(input("Enter 1 to exit.\nPress any key to continue.\n"))
        if(closer == '1'):
            return
                

