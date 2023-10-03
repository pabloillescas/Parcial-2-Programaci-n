import mysql.connector

conexion = mysql.connector.connect(user="root", password="root", host="localhost", database="basededatos", port="3306")

def añadir_tarea(descripcion):
    cursor = conexion.cursor()
    dato = "INSERT INTO tareas (Descripcion, Completada) VALUES (%s, %s)"
    valores = (descripcion, False)
    cursor.execute(dato, valores)
    conexion.commit()
    print("Tu tarea ha sido añadida!")

def completado(id_tarea):
    cursor = conexion.cursor()
    dato = "UPDATE tareas SET Completada = %s WHERE ID = %s"
    valores = (True, id_tarea)
    cursor.execute(dato, valores)
    conexion.commit()
    print("Tarea marcada como completada!")

def lista_de_tareas():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tareas WHERE Completada = 0")
    tareas = cursor.fetchall()
    if not tareas:
        print("No tienes tareas pendientes!")
    else:
        for tarea in tareas:
            print(f"ID: {tarea[0]}, Descripción: {tarea[1]}")

def eliminar(id_tarea):
    cursor = conexion.cursor()
    dato = "DELETE FROM tareas WHERE ID = %s"
    valores = (id_tarea)
    cursor.execute(dato, valores)
    conexion.commit()
    print("Tarea eliminada con éxito!")

while True:
    print("\nOpciones:")
    print("1. Añadir tarea")
    print("2. Marcar tarea como completada")
    print("3. Lista de tareas pendientes")
    print("4. Eliminar tarea")
    print("5. Terminar")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        descripcion = input("Ingrese la tarea: ")
        añadir_tarea(descripcion)
    elif opcion == "2":
        id_tarea = input("ID de la tarea a marcar como completada: ")
        completado(id_tarea)
    elif opcion == "3":
        lista_de_tareas()
    elif opcion == "4":
        id_tarea = input("ID de la tarea a eliminar: ")
        eliminar(id_tarea)
    elif opcion == "5":
        break
    else:
        print("Tu opción no es válida, intenta de nuevo.")

conexion.close()