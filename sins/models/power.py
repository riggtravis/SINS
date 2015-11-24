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
	UniqueConstraint,	# Power titles must be unique.
	orm
)

# Create a human readable slug in the url
from webhelpers2.text import urlify

class Power(Base):
	""" This class describes what powers can be granted to groups. """
	# Metadata
	__tablename__ = 'powers'
	
	# Keys
	power_id = Column(Integer, primary_key=True)
	title = Column(Unicode(30), unique=True, nullable=False)
	
	# Relationships
	# This member variable should probably have a norsk name.
	adepts = orm.relationship("Permission", backref="powers")
	
	@property
	def slug(self):
		""" Create a human readable slug that makes it easy to read the URL. """
		return urlify(self.title)