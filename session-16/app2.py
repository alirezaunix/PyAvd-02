from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///Person.db')
Base = declarative_base()

class Person(Base):
    __tablename__ = 'Person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    
class Book(Base):
    __tablename__ = 'Book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bookname=Column(String,nullable=False)
    writername = Column(String, nullable=False)
    IBNS = Column(Integer, nullable=False)
    publisher = Column(String, nullable=False)
    
Base.metadata.create_all(engine)

#Insert Data Into DB:
Session = sessionmaker(bind=engine)
session = Session()
person1 = Person(firstname="John", lastname="Doe", age=30)
person2 = Person(firstname="Jane", lastname="Smith", age=25)
person3 = Person(firstname="Emily", lastname="Jones", age=22)
session.add_all([person1, person2, person3])
session.commit()

#Export From DB
data=session.query(Person).all()
for item in data:
    print(item.firstname,item.lastname,item.age)