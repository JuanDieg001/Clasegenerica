from accessData.entities.estudianteModel import Estudiante
from accessData.conexionORM import Database
from dominio.entities.modelsOrm.estudiante_dto import EstudianteBase

class EstudianteService:
    def __init__(self, database: Database):
        self.db = database

    def create_student(self, est: EstudianteBase):
        session = self.db.get_session()
        db_estudiante = Estudiante(nombre = est.nombre, apellido = est.apellido, edad = est.edad, mail = est.mail, matricula = est.matricula, carrera = est.carrera)
        session.add(db_estudiante)
        session.commit()
        session.refresh(db_estudiante)
        session.close()
        return db_estudiante

    def get_student_all(self):
        session = self.db.get_session()
        personas = session.query(Estudiante).all()
        session.close()
        return personas


    def get_student(self, person_id):
        session = self.db.get_session()
        person = session.query(Estudiante).filter(Estudiante.id == person_id).first()
        session.close()
        return person


    def update_student(self, est: EstudianteBase):
        session = self.db.get_session()
        estudiante = session.query(Estudiante).filter(Estudiante.id == est.id).first()
        if est.nombre:
            estudiante.nombre = est.nombre
        if est.apellido:
            estudiante.apellido = est.apellido
        if est.edad:
            estudiante.edad = est.edad
        if est.mail:
            estudiante.mail = est.mail
        session.commit()
        session.refresh(estudiante)
        session.close()
        return estudiante


    def delete_student(self, person_id):
        session = self.db.get_session()
        person = session.query(Estudiante).filter(Estudiante.id == person_id).first()
        session.delete(person)
        session.commit()
        session.close()
        return {"message": "Deleted successfully"}
    

    def cerrarConexion(self):
        session = self.db.get_session()
        session.close()

