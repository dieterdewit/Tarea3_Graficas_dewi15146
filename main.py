import os
import sys

oscp = int(input("Ingrese 1 para generar todos los archivos, 0 para salir"))

if oscp == 1:
    os.system('python Line1.py')
    os.system('python Line2.py')
    os.system('python Line3.py')
    os.system('python Line4.py')
    os.system('python Cube1.py')
    os.system('python Cube2.py')

elif oscp == 0:
    sys.exit(0)
