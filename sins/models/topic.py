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

# The date should be human readable.
from webhelpers2.date import distance_of_time_in_words

# There should be a readable slug for the user's sake.
from webhelpers2.text import urlify

class Topic(Base):
	"""docstring"""
	# Metadata
	__tablename__ = 'topics'
	
	# Keys
	topic_id = Column(Integer, primary_key=True)
	
	# Foreign Keys
	forum_id = Column(Integer, ForeignKey('forums.forum_id'), nullable=False)
	
	# Attributes
	start_date = Column(DateTime, nullable=False)
	subject = Column(Unicode(140), nullable=False)
	sticky_status = Column(Boolean)
	
	# Relationships
	posts = orm.relationship("Post", backref='topics')
	
	# When the topic was posted should be human readable
	def start_in_words(self):
		return distance_of_time_in_words(
			self.start_date,
			datetime.datetime.utcnow()
		)
	
	# Create a slug that the user should be able to read.
	@property
	def slug(self):
		return urlify(self.subject)