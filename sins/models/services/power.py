import sqlalchemy

# Pagination shouldn't be necessary for powers since there will be so few.

from ..meta import DBSession
from ..power import Power

""" Power service

Classes:
* PowerRecordService
** This class provides methods for retrieving power records from the database.

"""

class PowerRecordService(object):
	""" This class retreives powers from the database. """
	
	@classmethod
	def all(cls):
		""" This function retreives all of the powers from the database. """
		return DBSession.query(Power).order_by(sqlalchemy.desc(Power.power_id))
	
	@classmethod
	def by_id(cls, id):
		""" This function retreives a specific power from the databse. """
		return DBSession.query(Power).filter(Power.power_id == id).first()