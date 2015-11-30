import sqlalchemy

# We don't need to paginate groups. There shouldn't be many.

from ..meta import DBSession
from ..group import Group

""" Group service 

Classes:
* GroupRecordService
** This class provides us with a way to query the database for group records.

"""

class GroupRecordService(object):
	""" This class retreives groups from the database. """
	
	@classmethod
	def all(cls):
		""" Get all of the groups from the database. """
		return DBSession.query(Group).order_by(sqlalchemy.desc(Group.group_id))
	
	@classmethod
	def by_id(cls, id):
		""" Get a specific group. """
		return DBSession.query(Group).filter(Group.group_id == id).first()
	
	@classmethod
	def by_title(cls, title):
		return DBSession.query(Group).filter(Group.title == title).first()
	
