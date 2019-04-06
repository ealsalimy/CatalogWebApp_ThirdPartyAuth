from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Categories, Items



# Connect to Database and create database session
engine = create_engine('sqlite:///ItemCatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Run this only once, to avoid repetition
#You can Add more Categories
'''
category1 = Categories( name='food')
category2 = Categories( name='clothes')
category3 = Categories( name='sports')
category4 = Categories( name='news')
category5 = Categories( name='stories')
category6 = Categories( name='movies')
session.add(category1)
session.add(category2)
session.add(category3)
session.add(category4)
session.add(category5)
session.add(category6)
session.commit()

print 'Categories Added!'


categories = session.query(Categories).all()
id_c = ''
for c in categories:
    if c.name == 'sports':
        id_c = c.id
new_item = Items(title='Swimming',
                 description='''Swimming is a great workout because you need to
                 move your whole body against the resistance of the water.
                 Swimming is a good all-round activity because it:
                 keeps your heart rate up but takes some of the impact stress
                 off your body builds endurance, muscle strength and cardiovascular
                 fitness helps maintain a healthy weight, healthy heart and lungs
                 tones muscles and builds strength provides an all-over body
                 workout, as nearly all of your muscles are used during swimming.''',
                 cat_id=id_c)
session.add(new_item)
session.commit()
'''
