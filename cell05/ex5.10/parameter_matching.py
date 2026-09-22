import sys
if len(sys.argv) < 2:
    print("none")
else:
    inp = sys.argv[1]
    parameter = input("What was the parameter? ")
    if parameter == inp:
        print("Good job!")
    else:
        print("Nope, sorry...")