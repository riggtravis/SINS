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

""" Topic model 

Classes:
* Topic
** Used to describe discussion topics users want to talk about.

"""

# The date should be human readable.
from webhelpers2.date import distance_of_time_in_words

# There should be a readable slug for the user's sake.
from webhelpers2.text import urlify

class Topic(Base):
	""" This class describes a topic that posts can be made to. """
	# Metadata
	__tablename__ = 'topics'
	
	# Keys
	topic_id = Column(Integer, primary_key=True)
	
	# Foreign Keys
	forum_id = Column(Integer, ForeignKey('forums.forum_id'), nullable=False)
	
	# Attributes
	# Do I really need the start_date? Shouldn't this be be stored in the posts.
	subject = Column(Unicode(140), nullable=False)
	sticky_status = Column(Boolean)
	
	# Relationships
	posts = orm.relationship("Post", backref='topics')
	
	# Functions	
	@property
	def slug(self):
		""" Create a slug for the URL that the user should be able to read. """
		return urlify(self.subject)