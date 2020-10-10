from math import log

def Init():
    while True:
        while True:
            try:
                a = float(input("Please enter the first number of the harmonic sequence. \n"))
                n = int(input("Please enter the length of the harmonic sequence. \n"))
                d = float(input("Please enter the common difference.\n"))
                break
            except:
                print("Invalid Character")
        
        value = []
        
        total = 0
        tn = "1/" + str(a +(n - 1) * d)
        
        for i in range(n):
            value.append(a+(i)*d)
            
        print("\nResults:")
        
        for i in range(len(value)):
            print(i + 1, " | 1/", value[i], sep='')
            total = total + (1/value[i])
            
        print('The sum of the harmonic sequence =', total)
        print('The nth term of the harmonic sequence =', tn)
        
        closer = str(input("\nEnter 1 to exit.\nPress any key to continue.\n"))
        if(closer == '1'):
            return
                

