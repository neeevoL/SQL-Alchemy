import sqlalchemy
import sqlalchemy.orm as orm

# does the magic so table's fields are mapped onto db in the right config
class Base(orm.DeclarativeBase, orm.MappedAsDataclass):
    pass


# Makes pupil class so pupils can be created (objects)
class Pupil(Base):
    __tablename__ = 'pupil'

    # time to create fields
    pupil_id: orm.Mapped[int] = orm.mapped_column(init = False,primary_key=True) # (init = False) used so argument not required to be entered in next file
    first_name: orm.Mapped[str] = orm.mapped_column()
    last_name: orm.Mapped[str] = orm.mapped_column()

    house_id: orm.Mapped[int] = orm.mapped_column(sqlalchemy.ForeignKey('house.house_id'), init=False, repr = False)
    house: orm.Mapped['House']=orm.relationship(default = None, back_populates='pupil')

# Makes house projects
class House(Base):
    __tablename__ = 'house'

    # time to create fields
    house_id: orm.Mapped[int] = orm.mapped_column(init = False, primary_key=True, repr = False) # (repr = False) so house ID isnt shown
    house_name: orm.Mapped[str] = orm.mapped_column()
    house_num_pupils: orm.Mapped[int] = orm.mapped_column()
    pupils = orm.Mapped[list[Pupil]]=orm.relationship(default_factory = list, back_populates='house', repr = False)
