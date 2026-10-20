from itertools import product

print("Bienvenido al curso de Codigo")

for credenciales_validas, no_esta_bloqueado, es_administrador in product([0, 1], repeat=3):

    if ((credenciales_validas and no_esta_bloqueado) or es_administrador):
        print(credenciales_validas, no_esta_bloqueado, es_administrador, " = 1" , "ACCESO PERMITIDO")
    else:
        print(credenciales_validas, no_esta_bloqueado, es_administrador, " = 0" , "ACCESO DENEGADO " )