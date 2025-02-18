from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///newPerson.db')
Base = declarative_base()


class Person(Base):
    __tablename__ = 'Person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

data = session.query(Person).filter(Person.age>65)
for item in data:
    print(item.firstname, item.lastname, item.age)
