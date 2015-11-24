import sqlalchemy
from paginate_sqlalchemy import SqlalchemyOrmPage	# For pagination purposes
from ..meta import DBSession
from ..forum import forum

# So I understand now why we need to have classmethods for each of the member
# functions. It seems to be that it's allowing this class to operate as a
# construtor of sorts for the forum class.

class ForumRecordService(object):
	"""docstring"""
	# Every class needs a minimum two functions. Those functions are:
	#	retrieve all records.
	@classmethod
	def all(cls):
		"""docstring"""
		return DBSession.query(Forum).order_by(sqlalchemy.desc(Forum.forum_id))
	
	#	retrieve record by id.
	@classmethod
	def by_id(cls, id):
		"""docstring"""
		return DBSession.query(Forum).filter(Forum.forum_id == id).first()
	
	# We need to retrieve the forums that have particular parents or no parents
	@classmethod
	def by_parent(cls, id):
		"""docstring"""
		return DBSession.query(Forum).filter(Forum.parent_id == id).order_by(Forum.forum_id)