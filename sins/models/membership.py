import datetime						# For default dates on models
from sins.models.meta import Base	# We need to import our metadata.

# Right now all of the datatypes will will need for any table is being imported
# every time. Before shipping a public release this should be fixed.
from sqlalchemy import (
	Column,
	Integer,
	Unicode,		# Provides Unicode field
	UnicodeText,	# Text field of unrestricted length
	Char,			# Fixed lenth strings
	Boolean,		# Provides true/false values
	DateTime,		# Time abstraction
	ForeignKey		# This table is needs to reference other tables.
)

class Membership(Base):
	# Metadata
	__tablename__ = 'memberships'
	
	# Keys
	user_id = Column(Integer, ForeignKey('people.user_id'), primary_key=True)
	group_id = Column(Integer, ForeignKey('groups.group_id'), primary_key=True)