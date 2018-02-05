#!/usr/bin/python3

import sys 


if sys.argv[1]=="multiplicar":
	final=float(sys.argv[2])*float(sys.argv[3])
elif sys.argv[1]=="dividir":
	final=float(sys.argv[2])/float(sys.argv[3])
elif sys.argv[1]=="sumar":
	final=float(sys.argv[2])+float(sys.argv[3])
elif sys.argv[1]=="restar":
	final=float (sys.argv[2])-float(sys.argv[3])

try:
	print ("El resultado es " + str(final))

except Error:
	print("Comando no admitido, introduczca: sumar, multiplicar, dividir o restar seguido de los dos operandos.")