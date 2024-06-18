import json

def registrar_trabajador(trabajadores):
    cargos = ["ceo","programador","analista"]
    while True:
        nombre = input("Ingrese Nombre_Apellido: ")
        cargo = input("Ingrese cargo (CEO/Programador/Analista): ").lower()
        if cargo in cargos:
            try:
                sueldo_bruto = int(input("Ingrese sueldo: "))
            except ValueError:
                print("Sueldo no es un numero, ingrese de nuevo")
            else:
                Desc_Salud = sueldo_bruto * 0.07
                Desc_AFP = sueldo_bruto * 0.12
                sueldo_liquido = sueldo_bruto - Desc_Salud - Desc_AFP
                #registro
                trabajadores.append({
                    'nombre': nombre,
                    'cargo': cargo,
                    'sueldo_bruto': sueldo_bruto,
                    'Desc_Salud': Desc_Salud,
                    'Desc_AFP': Desc_AFP,
                    'Sueldo_Liquido':sueldo_liquido
                })

                with open('datos.json','w') as archivo:
                    json.dump(trabajadores,archivo, indent=4)

                print("¿Deseas seguir agregando?")
                opcion = input("(s/n) ---> ").lower()
                if opcion == "n":
                    print("Saliendo... ")
                    break
                else:
                    print("Siguiente: ")
        else:
            print("cargo invalido, ingrese de nuevo")

def listar_trabajadores():
    
    with open('datos.json','r') as archivo:
        lector_datos = json.load(archivo)

        for trabajador in lector_datos:
            print(trabajador)


def imprimir_plantilla():
    cargos = ["ceo","programador","analista"]
    trabajadores_por_cargo = []

    with open('datos.json','r') as archivo:
            lector_datos = json.load(archivo)

    print("¿Desea imprimir todos?")
    opcion = input("(s/n) --> ").lower()
    if opcion == "n":
            opcion = input("¿Que cargo desea imprimir? (CEO/Programador/Analista): ")
            if opcion in cargos:
                
                for trabajador in lector_datos:
                    if trabajador['cargo'] == opcion:
                        trabajadores_por_cargo = trabajador
                        
                with open('cargos.json','w') as archivo:
                    json.dump(trabajadores_por_cargo,archivo,indent=4)
                    
            else:
                print("opcion invalida, ingrese de nuevo")
    else:

        for trabajador in lector_datos:
            print(trabajador)
