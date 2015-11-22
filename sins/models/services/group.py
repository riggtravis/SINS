import sqlalchemy

# We don't need to paginate groups. There shouldn't be many.

from ..meta import DBSession
from ..group import Group

class GroupRecordService(object):
	@classmethod
	def all(cls):
		return DBSession.query(Group).order_by(sqlalchemy.desc(Group.group_id))
	
	@classmethod
	def by_id(cls, id):
		return DBSession.query(Ban).filter(Ban.ban_id == id).first()