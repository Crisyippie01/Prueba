import funciones as fn
import time as tm
import os

trabajadores = []

while True: 
    print('''
                [- Menu - ]

            1. Registrar trabajador
            2. Listar todos los trabajadores
            3. Imprimir planilla de sueldos
            4. Salir del Programa
            ''')
    

    try:
       opcion = int(input("Opción: "))

    except ValueError:
        os.system('cls')
        print("Esa wea no e' un numero oe")
        tm.sleep(5)
        os.system('cls')
    else:
        if opcion == 1:
            fn.registrar_trabajador(trabajadores)
        elif opcion == 2:
            fn.listar_trabajadores()
        elif opcion == 3:
            fn.imprimir_plantilla()
        elif opcion == 4:
            os.system('cls')
            print("Saliendo.")
            tm.sleep(1)
            os.system('cls')
            print("Saliendo..")
            tm.sleep(1)
            os.system('cls')
            print("Saliendo...")
            tm.sleep(1)
            os.system('cls')
            break 
        
