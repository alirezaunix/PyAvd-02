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

# Insert Data Into DB:
Session = sessionmaker(bind=engine)
session = Session()

list_person=[]
for row in open("/Users/alireza/Desktop/pyadv-02/session-17/data.csv"):
    fname=row.split(",")[0]
    lname=row.split(",")[1]
    age=row.split(",")[2]
    list_person.append(Person(firstname=fname, lastname=lname, age=age))
    
    
session.add_all(list_person)
session.commit()
