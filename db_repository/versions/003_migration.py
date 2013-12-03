from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
brew = Table('brew', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('beer_id', Integer),
    Column('brew_date', Integer),
    Column('batch_size', Float),
    Column('abv', Float),
    Column('ibu', Integer),
)

keg = Table('keg', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('brew_id', Integer),
    Column('kegged_date', Integer),
    Column('volume', Float),
)

tap = Table('tap', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('keg_id', Integer),
    Column('location_id', Integer),
    Column('identifier', String),
)

beer = Table('beer', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('kegged_date', Integer),
    Column('abv', Float),
    Column('ibu', Integer),
)

beer = Table('beer', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=120)),
    Column('description', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['brew'].create()
    post_meta.tables['keg'].create()
    post_meta.tables['tap'].create()
    pre_meta.tables['beer'].columns['abv'].drop()
    pre_meta.tables['beer'].columns['ibu'].drop()
    pre_meta.tables['beer'].columns['kegged_date'].drop()
    post_meta.tables['beer'].columns['description'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['brew'].drop()
    post_meta.tables['keg'].drop()
    post_meta.tables['tap'].drop()
    pre_meta.tables['beer'].columns['abv'].create()
    pre_meta.tables['beer'].columns['ibu'].create()
    pre_meta.tables['beer'].columns['kegged_date'].create()
    post_meta.tables['beer'].columns['description'].drop()
