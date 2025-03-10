import sqlalchemy
import sqlalchemy.orm as orm
import model

engine = sqlalchemy.create_engine('sqlite+pysqlite:///pupils.sqlite')

with (orm.Session(engine)) as session:

    print("All the pupils")
    pupils = session.query(model.Pupil).all()
    print(pupils)
    # since pupils is a list of objects, you can do this:
    for pupil in pupils:
        print(pupil.first_name) # you can do things that you can do with objects! like show

    print("All the houses")
    houses = session.query(model.House).all()
    for house in houses:
        print(house.house_name)

    print("\nGet the ORM object for maths\n")
    maths_qry = (sqlalchemy.select(model.Subject).where(model.Subject.name == "Mathematics"))
    maths = session.scalar(maths_qry)
    print(maths)

    print(\n)

