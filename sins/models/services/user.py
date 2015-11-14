import sqlalchemy
from paginate_sqlalchemy import SqlalchemyOrmPage	# For pagination purposes
from ..meta import DBSession
from ..user import User

class UserRecordService(object):
	@classmethod
	def by_id(cls, id):
		return DBSession.query(Ban).filter(Ban.ban_id == id).first()