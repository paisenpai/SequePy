def Init():
    while True:
        err = False
        try:
            a = int(input("Please enter the first number of the arithmetic sequence. \n"))
            n = int(input("Please enter the total numbers in the arithmetic sequence. \n"))
            d = int(input("Please enter the common difference.\n"))
        except:
            print("Invalid Character")
            err = True

        if not err:
            total = (n * (2 * a + (n - 1) * d)) / 2
            tn = a + (n - 1 ) * d

            print('\nResult:')
            print('The sum of the arithmetic sequence = ', total)
            print('The nth term of the arithmetic sequence = ', tn, '\n')
            closer = str(input("Enter 1 to exit.\nPress any key to continue.\n"))
            if(closer == '1'):
                return
                