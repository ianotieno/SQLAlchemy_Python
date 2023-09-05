from sqlalchemy import create_engine, Column, String, Integer, CHAR
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


engine = create_engine('sqlite:///mydb.db', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# person = Person(999, "mike", "smith", "m", 23)
# session.add(person)
# session.commit()

# p1 = Person(987, "ian", "smith", "m", 23)
# p2 = Person(564, "paul", "smith", "f", 23)
# p3 = Person(533, "meek", "juger", "m", 23)
# session.add(p1)
# session.add(p2)
# session.add(p3)
# session.commit()
# new_person = Person(767, "John", "Doe", "m", 25)
# session.add(new_person)
# session.commit()

results = session.query(Person).all()
print(results)

results = session.query(Person).filter(Person.lastname == "smith")
for r in results:
    print(r)
esults = session.query(Person).filter(Person.firstname.like("% an %"))
for r in results:
    print(r)
