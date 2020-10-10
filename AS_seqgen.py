def Init():
    while True:
        total = 0
        tn = 0
        value = []
        while True:
            try:
                a = float(input("Please enter the first number of the sequence. \n"))
                n = int(input("Please enter the length of the sequence. \n"))
                assert n > 0
                d = float(input("Please enter the common difference.\n"))
                break
            except:
                print("Invalid Character")
        
        for i in range(n):
            value.append(a+(i)*d)
        
        print("\nResults:")
        for i in range(len(value)):
            print(i + 1, " | ", value[i])
            
        total = (n * (2 * a + (n - 1) * d)) / 2
        tn = a + (n - 1 ) * d
        print('The sum of the arithmetic sequence =', total)
        print('The nth term of the arithmetic sequence =', tn)
        
        closer = str(input("\nEnter 1 to exit.\nPress any key to continue.\n"))
        if(closer == '1'):
            return
                