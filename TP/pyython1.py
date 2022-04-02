from re import M


def Collatz(M):

    nbrlter=0

    while M!=1:

        if M%2==0:

            M=M//2

        else:

            M=3*M+1

        print (M)

    nbrlter+=1

    return (nbrlter)

var = Collatz (27)

print (var)
#FANTA
