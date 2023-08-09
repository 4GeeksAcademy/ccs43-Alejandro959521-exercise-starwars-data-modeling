import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True )
    name = Column(String(250), nullable=False)  
    email = Column(String(250),nullable=False,unique=True)
    password= Column(String(450), nullable=False)
    address= relationship("Address",back_populates="usuario")
    favoritos=relationship("Favoritos",back_populates="usuario")

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    usuario_id = Column(ForeignKey('usuario.id'))
    usuario = relationship("Usuario",back_populates="address")


class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    person_class = Column(String(250))
    faccion = Column(String(250))
    race = Column(String(250))
    gender = Column(String(250))
    favoritos = relationship("Favoritos",back_populates="personajes")

class Planetas(Base):    
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    size = Column(String(250))
    temp =  Column(Integer)
    color = Column(String(250))
    moon_numbers = Column(String(250))
    favoritos=relationship("Favoritos",back_populates="planetas")

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    type_vehicle = Column(String(250))
    color = Column(String(250))
    model = Column(String(250))
    brand = Column(String(250))
    price = Column(Integer)   
    passengers = Column(Integer)
    favoritos=relationship("Favoritos",back_populates="vehicles")

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(ForeignKey('vehicles.id'), nullable=True)
    vehicles = relationship("Vehicles",back_populates="favoritos") 
    #vehicle_favoritos = relationship(Vehicles)
    user_id = Column(ForeignKey('usuario.id'), nullable=True)
    usuario=relationship("Usuario",back_populates="favoritos") 
    #user_favoritos = relationship(Usuario)
    personaje_id = Column(ForeignKey('personajes.id'), nullable=True)
    personales=relationship("Personajes",back_populates="favoritos") 
    #personaje_favoritos = relationship(Personajes)
    planet_id = Column(ForeignKey('planetas.id'), nullable=True)
    planetas=relationship("Planetas",back_populates="favoritos") 
    #planet_favoritos = relationship(Planetas)        
    
   # def to_dict(self):
    #    return {}   

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
