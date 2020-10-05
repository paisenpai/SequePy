import arithseq
import pythagorean
import trianglearea

def main():
    while True:
        equationType = 0
        while True:
            # handling error for input
            try:
                # request user input
                equationType = int(input("Press 1 to use arithmetic"\
                " sequence\nPress 2 to use pythagorean theorem\n"\
                "Press 3 to use triangle area\n"))
                if not(equationType > 0 and equationType <= 3):
                    # check if input is within the choices,
                    # throws error if wrong input
                    raise(TypeError)
                else:
                    # releases while loop if success
                    break
            except:
                print('Please input a valid number')

        if (equationType == 1):
            arithseq.Init()
        elif (equationType == 2):
            pythagorean.Init()
        elif (equationType == 3):
            trianglearea.Init()
            
if __name__ == "__main__":
	main()