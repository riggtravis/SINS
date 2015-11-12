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
	UniqueConstraint,	# We need to ensure that forum titles are unique
	ForeignKey,			# The table needs to make a reference to itself.
	orm
)

# We have a slug that needs to be created when visiting the page.
from webhelpers2.text import urlify

class Forum(Base):
	# Metadata
	__tablename__ = 'forums'
	
	# Keys
	forum_id = Column(Integer, primary_key=True)
	title = Column(Unicode(30), unique=True, nullable=False)
	
	# Foreign Keys
	parent_id = Column(Integer, ForeignKey('forums.forum_id'))
	
	# Relationships
	children = orm.relationship("Forum")
	
	# It'd be nice to have a readable slug.
	@property
	def slug(self):
		return urlify(self.title)