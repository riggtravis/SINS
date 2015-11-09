import datetime						# For default dates on models
from sins.models.meta import Base	# We need to import our metadata.

# Right now all of the datatypes will will need for any table is being imported
# every time. Before shipping a public release this should be fixed.
from sqlalchemy import (
	Column,
	Integer,
	Unicode,		# Provides Unicode field
	UnicodeText,	# Text field of unrestricted length
	CHAR,			# Fixed length strings
	Boolean,		# Provides true/false values
	DateTime,		# Time abstraction
	ForeignKey,		# Allows tables to reference other tables.
	orm
)
from sqlalchemy.orm import relationship, backref

class Ban(Base):
	# Metadata
	__tablename__ = 'bans'
	
	# Keys
	ban_id = Column(Integer, primary_key=True)
	
	# Foreign Keys
	user_id = Column(Integer, ForeignKey('people.user_id'))