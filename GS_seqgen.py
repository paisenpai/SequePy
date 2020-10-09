from math import pow

def Init():
    while True:
        while True:
            try:
                a = float(input("Please enter the first number of the arithmetic sequence. \n"))
                n = int(input("Please enter the total numbers in the arithmetic sequence. \n"))
                r = float(input("Please enter the common ratio.\n"))
                break
            except:
                print("Invalid Character")

        value = []
        for i in range(n):
            value.append(a * pow(r, i))

        print("\nResults:")
        for i in value:
            print(i)

        closer = str(input("Enter 1 to exit.\nPress any key to continue.\n"))
        if(closer == '1'):
            return