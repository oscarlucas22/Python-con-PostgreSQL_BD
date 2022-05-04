import sys
import psycopg2
import psycopg2.extras

def Conectar_BD(host,usuario,password,nombrebd):
    try:
        db = psycopg2.connect(host="localhost",user="postgres",password="asdasd",database="Proyecto-Python")
        return db 
    except psycopg2.Error as e:
        print("No puedo conectar a la base de datos:",e)
        sys.exit(1)

def Desconectar_BD(db):
    db.close()
#1
def Mostrar_socios(db):
    print("-----------------------------------------------------")
    print("Informacion de los socios")
    print("-----------------------------------------------------")
    sql = "SELECT * FROM SOCIOS"
    cursor = db.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print("-- DNI:",registro["dni"],"-- Nombre:",registro["nombre"],"-- Direccion:",registro["direccion"])
    except:
        print("Error al hacer la consulta")
        db.rollback()
    print("\r")
    print("-----------------------------------------------------")
    print("Total de socios")
    print("-----------------------------------------------------")
    sql2 = "SELECT count(Nombre) FROM SOCIOS"
    cursor = db.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    try:
        cursor.execute(sql2)
        registros = cursor.fetchall()
        for registro in registros:
            print("-- El total de socios es:",registro["count"])
    except:
        print("Error al hacer la consulta")
        db.rollback()
#2
def nombre(db):
    sql="SELECT NombrePelicula FROM PELICULAS"
    cursor = db.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print("-- Nombre Pelicula:",registro["nombrepelicula"])
    except:
        print("Error al hacer la consulta")
def Mostrar_NombrePelicula(db):
    print("-----------------------------------------------------")
    print("Mostrar NombrePelicula que empiece por 'L'")
    print("-----------------------------------------------------")
    sql = "SELECT NombrePelicula FROM PELICULAS WHERE substr(NombrePelicula,1,1) = 'L'"
    cursor = db.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print("-- Nombre de la pelicula:",registro["nombrepelicula"])
    except:
        print("Error al hacer la consulta")
        db.rollback()
#3
def ano(db):
    sql="SELECT AnoEstreno, NombrePelicula FROM PELICULAS"
    cursor = db.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print("-- Año Estreno:",registro["anoestreno"],"-- Nombre Pelicula:",registro["nombrepelicula"])
    except:
        print("Error al hacer la consulta")
def Mostrar_NombrePeliculaHoy(db,anno):
    print("-----------------------------------------------------")
    print("Nombre de la pelicula del año introducido")
    print("-----------------------------------------------------")
    sql = "SELECT NombrePelicula FROM PELICULAS WHERE AnoEstreno = '%d'" % anno
    cursor = db.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print("No hay ninguna con ese año")
        else:
            registros = cursor.fetchall()
            for registro in registros:
                print("-- Nombre de la pelicula:",registro["nombrepelicula"])
    except psycopg2.Error as e:
        print("Error al hacer la consulta", e)
#4
def Insertar_Socio(db,socio):
    cursor = db.cursor()
    sql = "INSERT INTO SOCIOS VALUES ('%s', '%s', '%s')" % (socio["DNI"],socio["Nombre"],socio["Direccion"])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error al insertar.")
        db.rollback()
        print("\r")
    print("-----------------------------------------------------")
    print("Tabla SOCIOS")
    print("-----------------------------------------------------")
    sql2 = "SELECT * FROM SOCIOS"
    cursor = db.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    try:
        cursor.execute(sql2)
        registros = cursor.fetchall()
        for registro in registros:
            print("-- DNI:",registro["dni"],"-- Nombre:",registro["nombre"],"-- Direccion:",registro["direccion"])
    except:
        print("Error al hacer la consulta")
        db.rollback()
#5
def borrar(db):
    sql="SELECT DNI FROM SOCIOS"
    cursor = db.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print("-- DNI:",registro["dni"])
    except:
        print("Error al hacer la consulta")
def Borrar_Socio(db,d):
    sql = "DELETE FROM SOCIOS WHERE DNI='%s'" % d
    cursor = db.cursor()
    resp=input("¿Ralmente quieres borrar al alumno '%s'? (pulsa 's' para si)" % d)
    if resp=="s":
        try:
            cursor.execute(sql)
            db.commit()
            registros=cursor.fetchall()
            if cursor.rowcount==0:
                print("No hay socios con ese dni")
        except:
            print("Error al mostrar la consulta")
            db.rollback()
def borrar_dni(db):
    sql="SELECT DNI FROM SOCIOS"
    cursor = db.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print("-- DNI:",registro["dni"])
    except:
        print("Error al hacer la consulta")
#6
def dni(db):
    sql="SELECT DNI_fk, Importe FROM PRESTAMOS"
    cursor = db.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print("-- DNI:",registro["dni_fk"],"-- Importe:",registro["importe"])
    except:
        print("Error al hacer la consulta")
def Actualizar_Importe(db, importe, dni):
    print("-----------------------------------------------------")
    print("Actualizacion del importe")
    print("-----------------------------------------------------")
    sql = "UPDATE PRESTAMOS SET Importe=%d WHERE DNI_fk='%s'" % (importe,dni)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error al hacer la actualizacion")
        db.rollback()
    sql2 = "SELECT * FROM PRESTAMOS"
    cursor2 = db.cursor()
    try:
        cursor2.execute(sql2)
        registros=cursor2.fetchall()
        print("Asi se veria la tabla PRESTAMOS despues del proceso:")
        print("\r")
        for registro in registros:
            print(registro)
    except:
        print("Error al mostrar la consulta")

def MostrarMenu():
    menu = '''
1. Lista informacion de los socios e indica el total de socios
2. Muestra el nombre de las pelicula que empiece por L
3. Muestra el nombre de las peliculas que estan presentadas en el año introducido por teclado
4. Inserta en la tabla SOCIOS un nuevo registro que introduciras por teclado
5. Elimina el socio con el DNI que introduzcas por teclado
6. Escribe por teclado un nuevo importe y actualiza ese importe en la columna del dni que introduzcas por teclado
0. Salir del programa
'''

    print(menu)
    while True:
        try:
            opcion = int(input("Opcion: "))
            return opcion
        except:
            print("Opcion incorrecta, debe ser un numero")
