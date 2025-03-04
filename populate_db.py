import sqlalchemy
import sqlalchemy.orm as orm
import model

engine = sqlalchemy.create_engine('sqlite+pysqlite:///pupils.sqlite')

# opening 'door' to database so we can interact
with (orm.Session(engine)) as session:

    #create houses
    h1 = model.House(name="Northgate")
    h2 = model.House(name="Southgate")
    h3 = model.House(name="Queensgate")

    # add houses to session (db)

    session.add(h1)
    session.add(h2)
    session.add(h3)


    # create pupil as objects - these are records
    pupil_Th = model.Pupil(first_name = 'Teo', last_name = 'Hadjiniklov')
    pupil_Rc = model.Pupil(first_name='Ryan', last_name='Chan')
    pupil_Lk = model.Pupil(first_name='Loveen', last_name='Kishore')
    pupils.Ad = model.Pupil(first_name='Arthur', last_name='Dunno')

    # add pupils to session (db)
    session.add(pupil_Th)
    session.add(pupil_Rc)
    session.add(pupil_Lk)
    session.add(pupil_Ad)

    # essentially closing db
    session.commit()