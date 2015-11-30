import sqlalchemy
from paginate_sqlalchemy import SqlalchemyOrmPage	# For pagination purposes
from ..meta import DBSession
from ..user import User

""" User service

Classes:
* UserRecordService
** This class provides methods for fof retreiving user records from the databases

"""

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
	
	# Usernames are easier to remember than primary keys, and it will be useful
	# to get users by their username sometimes.
	@classmethod
	def by_username(cls, username):
		return DBSession.query(User).filter(User.username == username).first()
	
