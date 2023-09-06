from sqlalchemy import create_engine, Column, String, Integer, CHAR,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    ssn = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    gender = Column(CHAR)
    age = Column(Integer)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"Person({self.ssn}, {self.firstname}, {self.lastname}, {self.gender}, {self.age})"

class Thing(Base):
    __tablename__ ="things"

    tid=Column("tid",Integer,primary_key=True)
    description=Column("description",String)
    owner =Column(Integer,ForeignKey("people.ssn"))

    def __init__(self,tid,description,owner):
        self.tid=tid
        self.description=description
        self.owner=owner

    def __repr__ (self):
        return f"({self.tid},{self.description},owned by {self.owner})"    


engine = create_engine('sqlite:///mydb.db', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# person = Person(999, "mike", "smith", "m", 23)
# session.add(person)
# session.commit()

p1 = Person(980, "oti", "smith", "m", 23)
p2 = Person(5770, "paul", "smith", "f", 23)
p3 = Person(5230, "meek", "juger", "m", 23)
session.add_all([p1,p2,p3])
session.commit()
new_person = Person(767, "John", "Doe", "m", 25)
session.add(new_person)
session.commit()

t1=Thing(60,"laptop",p1.ssn)
t2=Thing(170,"phone",p2.ssn)
t3=Thing(180,"key",p3.ssn)
t4=Thing(100,"tv",p1.ssn)


session.add_all([t1,t2,t3,t4])
session.commit()

results = session.query(Person).all()
print(results)

results = session.query(Person).filter(Person.lastname == "smith")
for r in results:
    print(r)
results = session.query(Thing,Person).filter(Thing.owner == Person.ssn)
for r in results:
    print(r)

