import sqlalchemy
from paginate_sqlalchemy import SqlalchemyOrmPage	# For pagination purposes
from ..meta import DBSession
from ..user import User

class UserRecordService(object):
	""" This class retrieves users from the database. """
	
	@classmethod
	def all(cls):
		""" This function retreives all of the users in the database. """
		return DBSession.query(User).order_by(sqlalchemy.desc(User.join_date))
	
	@classmethod
	def by_id(cls, id):
		""" This function retreives a specific user from the database. """
		return DBSession.query(User).filter(User.user_id == id).first()