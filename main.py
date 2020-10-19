import AS_calc
import pythagorean
import trianglecalc_area
import AS_seqgen
import AS_difference
import GS_seqgen
import HS_seqgen
import FS_seqgen
import AlgePy

def main():
    while True:
        equationType = 0
        while True:
            # handling error for input
            try:
                # request user input
                equationType = int(input(
                "Press 1 to generate arithmetic sequence,\nsum and nth term, d is found\n"
                "Press 2 to find difference of and, \nsum of an arithmetic sequence, An is found\n"
                "Press 3 to generate geometric sequence\n"
                "Press 4 to generate harmonic sequence\n"
                "Press 5 to generate fibonacci sequence\n"
                "Press 6 to use pythagorean theorem\n"
                "Press 7 to get area of triangle\n"
                "Press 8 to use Algebra Mode\n"))
                if not(equationType > 0 and equationType <= 8):
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
        	AS_difference.Init()
        elif (equationType == 3):
            GS_seqgen.Init()
        elif (equationType == 4):
            HS_seqgen.Init()
        elif(equationType == 5):
            FS_seqgen.Init()
        elif(equationType == 6):
            pythagorean.Init()
        elif(equationType == 7):
            trianglecalc_area.Init()
        elif(equationType == 8):
            AlgePy.Init()
            
if __name__ == "__main__":
	main()