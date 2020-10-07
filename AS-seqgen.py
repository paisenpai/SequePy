def Init():
        while True:
            err = False
            try:
                a = int(input("Please enter the first number of the sequence. \n"))
                n = int(input("Please enter the length of the sequence. \n"))
                d = int(input("Please enter the common difference.\n"))
            except:
                print("Invalid Character")
                err = True
            if not err:
                value = []
                for i in range(n):
                    value.append(a+(i)*d)
                for i in value:
                    print(i)
            closer = str(input("Enter 1 to exit.\nPress any key to continue.\n"))
            if(closer == '1'):
                return
                
