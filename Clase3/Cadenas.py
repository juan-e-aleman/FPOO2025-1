# Realice un programa que permita mediante un menu: Capturar la informacion de estudiantes (nombres, apellidos, edad), nos debe permitir ver cual es el estudiante mas joven y el mas viejo.
# Adicionalmente el programa debe permitirnos ver la informacion de todos los estudiantes registrados.

# .format{}, 
#	split, join
# "{} tiene {} manzanas".format(nombre, cantidad)
# Usando F-Strings f"{nombre} tiene {cantidad} manzanas"
# for numero in numeros:

def menu():
    print("1. Ingresar estudiante")
    print("2. Ver estudiante mas joven")
    print("3. Ver estudiante mas viejo")
    print("4. Ver todos los estudiantes")
    print("5. Salir")
    opcion = input("Ingrese una opcion: ")
    return opcion

def ingresar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    estudiantes.append({"nombre": nombre, "apellido": apellido, "edad": edad})
    return estudiantes

def estudiante_mas_joven(estudiantes):   
    estudiante_mas_joven = estudiantes[0]
    for estudiante in estudiantes:
        if estudiante["edad"] < estudiante_mas_joven["edad"]:
            estudiante_mas_joven = estudiante
    return estudiante_mas_joven


def estudiante_mas_viejo(estudiantes):
    estudiante_mas_viejo = estudiantes[0]
    for estudiante in estudiantes:
        if estudiante["edad"] > estudiante_mas_viejo["edad"]:
            estudiante_mas_viejo = estudiante
    return estudiante_mas_viejo

def ver_estudiantes(estudiantes):
    for estudiante in estudiantes:
        print("Nombre: {} Apellido: {} Edad: {}".format(estudiante["nombre"], estudiante["apellido"], estudiante["edad"]))

def main():
    estudiantes = []
    while True:
        opcion = menu()
        if opcion == "1":
            estudiantes = ingresar_estudiante(estudiantes)
        elif opcion == "2":
            try:
                estudiante = estudiante_mas_joven(estudiantes)
                print(f"El estudiante mas joven es: {estudiante["nombre"]} {estudiante["apellido"]} con {estudiante["edad"]} años")
            except:
                print("No hay estudiantes registrados")
        elif opcion == "3":
            estudiante = estudiante_mas_viejo(estudiantes)
            print("El estudiante mas viejo es: {} {} con {} años".format(estudiante["nombre"], estudiante["apellido"], estudiante["edad"]))
        elif opcion == "4":
            ver_estudiantes(estudiantes)
        elif opcion == "5":
            break
        else:
            print("Opcion invalida")

main()

