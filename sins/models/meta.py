from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

from zope.sqlalchemy import ZopeTransactionExtension

# I know this docstring is necessary because this file is used as a module.
""" Meta docstring

Objects:
********

* DBSession
** Used to make queries to the database.
* Base
** Used as a base class for the model classes.

"""

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()