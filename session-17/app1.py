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
    
Base.metadata.create_all(engine)

#Insert Data Into DB:
Session = sessionmaker(bind=engine)
session = Session()
#person1 = Person(firstname="John", lastname="Doe", age=30)
#person2 = Person(firstname="Jane", lastname="Smith", age=25)
#person3 = Person(firstname="Emily", lastname="Jones", age=22)
#session.add_all([person1, person2, person3])
#session.commit()

#Export From DB
#data=session.query(Person).all()
#for item in data:
#    print(item.firstname,item.lastname,item.age)
    
    
#data = session.query(Person).filter(Person.age>24 , Person.age < 28)
#for item in data:
#    print(item.firstname, item.lastname,item.age)


#data = session.query(Person).filter(Person.firstname.like('J%'),Person.age<30)
#for item in data:
#    print(item.firstname, item.lastname,item.age)

data = session.query(Person).order_by(Person.age.asc())
for item in data:
    print(item.firstname, item.lastname,item.age)
