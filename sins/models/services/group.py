import sqlalchemy

# We don't need to paginate groups. There shouldn't be many.

from ..meta import DBSession
from ..group import Group

class GroupRecordService(object):
	"""docstring"""
	@classmethod
	def all(cls):
		"""docstring"""
		return DBSession.query(Group).order_by(sqlalchemy.desc(Group.group_id))
	
	@classmethod
	def by_id(cls, id):
		"""docstring"""
		return DBSession.query(Ban).filter(Ban.ban_id == id).first()