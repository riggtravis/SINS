import sqlalchemy
from paginate_sqlalchemy import SqlalchemyOrmPage	# For pagination purposes
from ..meta import DBSession
from ..topic import Topic

class ForumRecordService(object):
	# Every class needs a minimum two functions. Those functions are:
	#	retrieve all records.
	@classmethod
	def all(cls):
		return DBSession.query(Forum).order_by(sqlalchemy.desc(Forum.forum_id))
	
	#	retrieve record by id.
	@classmethod
	def by_id(cls, id):
		return DBSession.query(Forum).filter(Forum.forum_id == id).first()
	
	# We need to retrieve the forums that have particular parents or no parents
	@classmethod
	def by_parent(cls, id):
		return DBSession.query(Forum).filter(Forum.parent_id == id).order_by(Forum.forum_id)