from __future__ import print_function
import psutil
import string
from timeit import timeit
from time import time

def main():


    mykey = input("Ingrese la llave > ")
    #mykey="ULIMA"

    input_text = input("Ingrese la cadena a cifrar > ")
    #input_text="SEGURIDAD DE LA INFORMACION"

    code_text = input("Ingrese el code_text > ")
    # code_text="NOÑGRCÑIO DY VI TNZZZXAWSWY"

    # Alphabet used as reference (M)

    # ABCDEFGHIJKLMNOPQRSTUVWXYZ

    source = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


    # Key alphabet (K) shifted 1 position to the left

    # BCDEFGHIJKLMNOPQRSTUVWXYZA

    shift = 0

    matrix = [ source[(i + shift) % 27] for i in range(len(source)) ]

    tiempo_inicial = time() 

    def coder(thistext):

        ciphertext = []

        control = 0

    

        for x,i in enumerate(input_text.upper()):

            if i not in source:

                #If the symbol is not in our reference alphabet, we simply print it

                ciphertext.append(i)

                continue

            else:

                #Wrap around the mykey string

                control = 0 if control % len(mykey) == 0 else control

    

                #Calculate the position C[i] = (M[i]+K[i]) mod len(M)

                result = (source.find(i) + matrix.index(mykey[control])) % 27

    

                #Add the symbol in position "result" to be printed later

                ciphertext.append(matrix[result])

                control += 1

    

        return ciphertext

    tiempo_final = time() 


    tiempo_inicial2 = time() 

    def decoder(thistext):

        control = 0

        plaintext = []

    

        for x,i in enumerate(code_text.upper()):

            if i not in source:

                #If the symbol is not in our reference alphabet, we simply print it

                plaintext.append(i)

                continue

            else:

                #Wrap around the mykey string

                control = 0 if control % len(mykey) == 0 else control

    

                #Calculate the position M[i] = (C[i]-K[i]) mod len(M)

                result = (matrix.index(i) - matrix.index(mykey[control])) % 27

    

                #Add the symbol in position "result" to be printed later

                plaintext.append(source[result])

                control += 1

    

        return plaintext


    tiempo_final2 = time() 

    # Print results

    print("Key: {0}".format(mykey))

    print("\nDecode text:")

    print("-> Input text: {0}".format(input_text))

    print("-> Coded text: {0}".format(''.join(coder(input_text))))

    

    # Print results

    print("\nDecode text:")

    print("-> Input text: {0}".format(code_text))

    print("-> Decoded text: {0}".format(''.join(decoder(code_text)).lower()))


    print("\nTiempo del cifrado")
    print(tiempo_final - tiempo_inicial)

    print("\nTiempo del descifrado")
    print(tiempo_final2 - tiempo_inicial2)


    print("\nCPU:", psutil.cpu_percent())
    print("\nMEMORIA:", psutil.virtual_memory())


    
main()


