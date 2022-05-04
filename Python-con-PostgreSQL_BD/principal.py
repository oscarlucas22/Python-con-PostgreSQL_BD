from funciones import *

db = psycopg2.connect(host="localhost",user="postgres",password="asdasd",database="Proyecto-Python")
opcion = MostrarMenu()

while opcion != 0:
    if opcion == 1:
        Mostrar_socios(db)

    elif opcion == 2:
        print("-----------------------------------------------------")
        print("Los nombres de las peliculas de la tabla PELICULAS")
        print("-----------------------------------------------------")
        nombre(db)
        print()
        Mostrar_NombrePelicula(db)

    elif opcion == 3:
        print("-----------------------------------------------------")
        print("Los años de estreno de la tabla PELICULAS")
        print("-----------------------------------------------------")
        ano(db)
        print()
        anno = int(input("Año de Estreno:"))
        Mostrar_NombrePeliculaHoy(db,anno)

    elif opcion == 4:
        print("-----------------------------------------------------")
        print("Insercion de socio")
        print("-----------------------------------------------------")
        socio={}
        socio["DNI"]=input("DNI:")
        socio["Nombre"]=input("Nombre:")
        socio["Direccion"]=input("Direccion:")
        Insertar_Socio(db,socio)

    elif opcion == 5:
        print("-----------------------------------------------------")
        print("Los dni de la tabla SOCIOS")
        print("-----------------------------------------------------")
        borrar(db)
        print()
        d=input("Introduce un DNI para borrar la columna correspondiente a este:")
        Borrar_Socio(db,d)
        print("-----------------------------------------------------")
        print("Los dni de la tabla SOCIOS despues del proceso de borrado")
        print("-----------------------------------------------------")
        borrar_dni(db)
        print()

    elif opcion == 6:
        print("-----------------------------------------------------")
        print("Los dni y los importes de la tabla PRESTAMOS")
        print("-----------------------------------------------------")
        dni(db)
        print()
        impot=int(input("Nuevo Importe a introducir:"))
        d=input("Introduce un DNI para actualizar la columna del importe correspondiente a este:")
        Actualizar_Importe(db,impot,d)

    else:
        print("Opcion incorrecta.")

    opcion=MostrarMenu()
print("Ha salido del programa")
Desconectar_BD(db)
