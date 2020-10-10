import AS_calc
import pythagorean
import trianglecalc_area
import AS_seqgen
import GS_seqgen
import HS_seqgen
import FS_seqgen

def main():
    while True:
        equationType = 0
        while True:
            # handling error for input
            try:
                # request user input
                equationType = int(input(
                "Press 1 to generate arithmetic sequence\n"
                "Press 2 to generate geometric sequence\n"
                "Press 3 to generate harmonic sequence\n"
                "Press 4 to generate fibonacci sequence\n"
                "Press 5 to use pythagorean theorem\n"
                "Press 6 to get area of triangle\n"))
                if not(equationType > 0 and equationType <= 7):
                    # check if input is within the choices,
                    # throws error if wrong input
                    raise(TypeError)
                else:
                    # releases while loop if success
                    break
            except:
                print('Please input a valid number')

        if (equationType == 1):
            AS_seqgen.Init()
        elif (equationType == 2):
            GS_seqgen.Init()
        elif (equationType == 3):
            HS_seqgen.Init()
        elif(equationType == 4):
            FS_seqgen.Init()
        elif(equationType == 5):
            pythagorean.Init()
        elif(equationType == 6):
            trianglecalc_area.Init()
            
if __name__ == "__main__":
	main()