from accessData.conexionORM import Database  # Importar la clase Database
from accessData.entities.estudianteModel import BaseDeDatos
from dominio.entities.modelsOrm.estudiante_dto import EstudianteBase  # Importar el DTO EstudianteDto
from servicio.estudiante_service import EstudianteService

DATABASE_URL = "mysql+mysqlconnector://root:admin@localhost:3307/instituto"

def main():
    estudiante_service = EstudianteService(db)

    while True:
        print("\n--- MENU ---")
        print("1. Crear estudiante")
        print("2. Mostrar todos estudiantes")
        print("3. Mostrar estudiante")
        print("4. Actualizar estudiante")
        print("5. Eliminar estudiante")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            edad = int(input("Ingrese la edad: "))
            mail = input("Ingrese el correo electrónico: ")
            matricula = input("Ingrese la matricula: ")
            carrera = input("Ingrese la carrera: ")

            student_dto = EstudianteBase(None, nombre, apellido, edad, mail, matricula, carrera)
            estudiante_service.create_student(student_dto)
            print(vars(student_dto))

        elif opcion == "2":
            estudiante = estudiante_service.get_student_all()
            for estudiante in estudiante:
                print(f"ID: {estudiante.id}, Nombre: {estudiante.nombre}, Apellido: {estudiante.apellido}, Edad: {estudiante.edad}, Mail: {estudiante.mail}, Matrícula: {estudiante.matricula}, Carrera: {estudiante.carrera}")
            
            
         

        elif opcion == "3":
            estudiante_id = int(input("Ingrese el ID del estudiante a consultar: "))
            estudiante = estudiante_service.get_student(estudiante_id)
            if estudiante:
                print(f"ID: {estudiante.id}, Nombre: {estudiante.nombre}, Apellido: {estudiante.apellido}, Edad: {estudiante.edad}, Mail: {estudiante.mail}, Matrícula: {estudiante.matricula}, Carrera: {estudiante.carrera}")
            else:
                print("Estudiante no encontrado")

        elif opcion == "4":
            id_estudiante = int(input("Ingrese el ID del estudiante que desea actualizar: "))
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            edad = int(input("Ingrese la nueva edad: "))
            mail = input("Ingrese el nuevo correo electrónico: ")
            matricula = input("Ingrese la matricula: ")
            carrera = input("Ingrese la carrera: ")
            student = EstudianteBase(id_estudiante, nombre, apellido, edad, mail, matricula, carrera)
            estudiante_service.update_student(student)
            print("Estudiante actualizado")

        elif opcion == "5":
            estudiante_id = int(input("Ingrese el ID del estudiante que desea eliminar: "))
            estudiante_service.delete_student(estudiante_id)
            print("Estudiante eliminado")

        elif opcion == "6":
            estudiante_service.cerrarConexion()
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    db = Database(DATABASE_URL)
    engine = db.engine
    BaseDeDatos.metadata.create_all(bind=engine)
    main()
           
