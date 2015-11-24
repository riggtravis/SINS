import sqlalchemy
from paginate_sqlalchemy import SqlalchemyOrmPage	# For pagination purposes
from ..meta import DBSession
from ..forum import forum

""" Forum service 

Classes:
* ForumRecordService
** This class provides functions that can be used to query the database.

"""

# So I understand now why we need to have classmethods for each of the member
# functions. It seems to be that it's allowing this class to operate as a
# construtor of sorts for the forum class.

class ForumRecordService(object):
	""" This class retrieves forums from the database. """

	@classmethod
	def all(cls):
		""" This function retreives all of the forums. """
		return DBSession.query(Forum).order_by(sqlalchemy.desc(Forum.forum_id))
	
	@classmethod
	def by_id(cls, id):
		""" This function retrieves a specific forum. """
		return DBSession.query(Forum).filter(Forum.forum_id == id).first()
	
	# We need to retrieve the forums that have particular parents or no parents
	@classmethod
	def by_parent(cls, id):
		""" This function retreives all of the forums with the same parent. """
		return DBSession.query(Forum).filter(Forum.parent_id == id).order_by(Forum.forum_id)