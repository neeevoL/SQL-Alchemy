import sqlalchemy
import sqlalchemy.orm as orm
import model

engine = sqlalchemy.create_engine('sqlite+pysqlite:///pupils.sqlite')

# opening 'door' to database so we can interact
with (orm.Session(engine)) as session:

    # create pupil as objects - these are records
    pupil_Th = model.Pupil(first_name = 'Teo', last_name = 'Hadjiniklov')
    pupil_Rc = model.Pupil(first_name='Ryan', last_name='Chan')

    # add pupils to session (db)
    session.add(pupil_Th)
    session.add(pupil_Rc)

    # essentially closing db
    session.commit()