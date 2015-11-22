import sqlalchemy

# Pagination shouldn't be necessary for powers since there will be so few.

from ..meta import DBSession
from ..power import Power

class PowerRecordService(object):
	@classmethod
	def all(cls):
		return DBSession.query(Power).order_by(sqlalchemy.desc(Power.power_id))
	
	@classmethod
	def by_id(cls, id):
		return DBSession.query(Power).filter(Power.power_id == id).first()