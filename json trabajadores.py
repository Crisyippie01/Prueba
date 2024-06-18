import funciones as fn
    
trabajadores = []

while True: 
    print('''
                [- Menu - ]

            1. Registrar trabajador
            2. Listar todos los trabajadores
            3. Imprimir planilla de sueldos
            4. Salir del Programa
            ''')
    opcion = int(input("Opción: "))

    if opcion == 1:
        fn.registrar_trabajador(trabajadores)
    elif opcion == 2:
        fn.listar_trabajadores()
    elif opcion == 3:
        fn.imprimir_plantilla()
    elif opcion == 4:
        print("Saliendo.")
        print("Saliendo..")
        print("Saliendo...")
        break 