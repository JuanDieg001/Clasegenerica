from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

BaseDeDatos = declarative_base()

class Estudiante(BaseDeDatos):
    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    edad = Column(Integer)
    mail = Column(String(50))
    matricula = Column(String(50))
    carrera = Column(String(50))

# Define la URL de conexión a la base de datos
DATABASE_URL = "mysql+mysqlconnector://root:admin@localhost:3307/instituto"

# Crea el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crea todas las tablas en la base de datos
BaseDeDatos.metadata.create_all(engine)

print("Tablas creadas exitosamente.")
