import datetime						# For default dates on models
from sins.models.meta import Base	# We need to import our metadata.

# Right now all of the datatypes will will need for any table is being imported
# every time. Before shipping a public release this should be fixed.
from sqlalchemy import (
	Column,
	Integer,
	Unicode,		# Provides Unicode field
	UnicodeText,	# Text field of unrestricted length
	CHAR,			# Fixed lenth strings
	Boolean,		# Provides true/false values
	DateTime,		# Time abstraction
	ForeignKey,		# Topics must be part of forums.
	orm
)

class Topic(Base):
	# Metadata
	__tablename__ = 'topics'
	
	# Keys
	topic_id = Column(Integer, primary_key=True)
	
	# Foreign Keys
	forum_id = Column(Integer, ForeignKey('forums.forum_id'), nullable=False)
	
	# Attributes
	subject = Column(Unicode(140), nullable=False)
	sticky_status = Column(Boolean)
	
	# Relationships
	posts = orm.relationship("Post", backref='topics')