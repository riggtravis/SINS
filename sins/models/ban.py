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

# The date should be human readable.
from webhelpers2.date import distance_of_time_in_words

""" Ban model

Classes:
* Ban
** Used to describe a user ban in which a user loses access to the community.

"""

class Ban(Base):
	""" This class describes bans that have been put on users. """
	# Metadata
	__tablename__ = 'bans'
	
	# Keys
	ban_id = Column(Integer, primary_key=True)
	
	# Foreign Keys
	user_id = Column(Integer, ForeignKey('people.user_id'), nullable=False)
	
	# Attributes
	start_date = Column(DateTime, nullable=False)
	end_date = Column(DateTime)
	reason = Column(UnicodeText, nullable=False)
	
	# Display dates in a human readable format.
	@property
	def start_in_words(self):
		""" This function is to display when the user got banned. """
		return distance_of_time_in_words(
			self.start_date,
			datetime.datetime.utcnow()
		)
	
	@property
	def end_in_words(self):
		""" This function is to display when the user will be reinstated. """
		return distance_of_time_in_words(
			self.end_date,
			datetime.datetime.utcnow()
		)