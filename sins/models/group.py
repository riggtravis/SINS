import datetime						# For default dates on models
from sins.models.meta import Base	# We need to import our metadata.

# Right now all of the datatypes will will need for any table is being imported
# every time. Before shipping a public release this should be fixed.
from sqlalchemy import (
	Column,
	Integer,
	Unicode,			# Provides Unicode field
	UnicodeText,		# Text field of unrestricted length
	CHAR,				# Fixed lenth strings
	Boolean,			# Provides true/false values
	DateTime,			# Time abstraction
	UniqueConstraint,	# Titles must be unique
	orm
)

# We should display a slug when the user visits.
from webhelpers2.text import urlify

class Group(Base):
	""" This class describes groups of users who can be asssigned powers. """
	# Metadata
	__tablename__ = 'groups'
	
	# Keys
	group_id = Column(Integer, primary_key=True)
	title = Column(Unicode(30), unique=True, nullable=False)
	
	# Relationships
	members = orm.relationship("Membership", backref="groups")
	permissions = orm.relationship("Permission", backref="groups")
	
	@property
	def slug(self):
		""" Create a human readable URL for when a user visits. """
		return urlify(self.title)