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
	UniqueConstraint,	# We need to ensure that usernames are unique.
	orm
)

# The date should be human readable.
from webhelpers2.date import distance_of_time_in_words

# We also have a slug that needs to be created.
from webhelpers2.text import urlify

class User(Base):
	# Metadata
	__tablename__ = 'people'
	
	# Keys
	user_id = Column(Integer, primary_key=True)
	username = Column(Unicode(30), unique=True, nullable=False)
	email_address = Column(Unicode(254), unique=True, nullable=False)
	
	# Attributes
	password = Column(CHAR(256), nullable=False)
	avatar = Column(CHAR(5))
	signature = Column(UnicodeText)
	bio = Column(UnicodeText)
	join_date = Column(DateTime, nullable=False)
	
	# Relationships
	bans = orm.relationship("Ban", backref="people")
	memberships = orm.relationship("Membership", backref="people")
	posts = orm.relationship("Post", backref="people")
	
	# The date the user joined should be human readable
	@property
	def joined_in_words(self):
		return distance_of_time_in_words(
			self.join_date,
			datetime.datetime.utcnow()
		)
	
	# There should be a nice readable slug when the user visitss.
	@property
	def slug(self):
		return urlify(self.username)