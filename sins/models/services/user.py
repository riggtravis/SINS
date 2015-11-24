import sqlalchemy
from paginate_sqlalchemy import SqlalchemyOrmPage	# For pagination purposes
from ..meta import DBSession
from ..user import User

class UserRecordService(object):
	"""docstring"""
	@classmethod
	def by_id(cls, id):
		"""docstring"""
		return DBSession.query(Ban).filter(Ban.ban_id == id).first()