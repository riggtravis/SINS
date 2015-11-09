import datetime						# For default dates on models
from sins.models.meta import Base	# We need to import our metadata.

# Right now all of the datatypes will will need for any table is being imported
# every time. Before shipping a public release this should be fixed.
from sqlalchemy import (
	Column,
	Integer,
	Unicode,			# Provides Unicode field
	UnicodeText,		# Text field of unrestricted length
	Char,				# Fixed lenth strings
	Boolean,			# Provides true/false values
	DateTime,			# Time abstraction
	UniqueConstraint	# We need to ensure that usernames are unique.
)

class User(Base):
	# Metadata
	__tablename__ = 'people'
	
	# Keys
	user_id = Column(Integer, primary_key=True)
	username = Column(Unicode(30), unique=True, nullable=False)
	
	# Attributes
	password = Column(Char(256), nullable=False)
	avatar = Column(Char(5))
	signature = Column(UnicodeText)
	
	# Relationships
	bans = relationship("Ban", backref="people")
	memberships = relationship("Membership", backref="people")
	posts = relationship("Post", backref="people")