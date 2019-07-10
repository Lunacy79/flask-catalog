from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import User, Base, Category, Item

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Items for Mamals
category1 = Category(categoryname='Mamals')

session.add(category1)
session.commit()


item1 = Item(itemname="Cat", description="Cute mamal with paws", category=category1)

session.add(item1)
session.commit()

item2 = Item(itemname="Dog", description="Cute mamal with four legs and two eyes", category=category1)

session.add(item2)
session.commit()

item3 = Item(itemname="Rabbit", description="Cute mamal with two ears", category=category1)

session.add(item3)
session.commit()

item4 = Item(itemname="Mouse", description="Tiny mamal with a nose", category=category1)

session.add(item4)
session.commit()



# Items for Birds
category2 = Category(categoryname='Birds')

session.add(category2)
session.commit()


item1 = Item(itemname="Parrot", description="Large bird with a beak", category=category2)

session.add(item1)
session.commit()

item2 = Item(itemname="Budgie", description="Tiny bird with beautiful colors", category=category2)

session.add(item2)
session.commit()



# Items for Reptiles
category3 = Category(categoryname='Reptiles')

session.add(category3)
session.commit()


item1 = Item(itemname="Frog", description="Cute mamal with paws", category=category3)

session.add(item1)
session.commit()

item2 = Item(itemname="Chameleon", description="Cute reptile with eyes going in seperate directions", category=category3)

session.add(item2)
session.commit()

item3 = Item(itemname="Salamander", description="Fast reptile with long tail", category=category3)

session.add(item3)
session.commit()


print("added items!")