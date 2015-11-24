import sqlalchemy
from paginate_sqlalchemy import SqlalchemyOrmPage	# For pagination purposes
from ..meta import DBSession
from ..ban import Ban

class BanRecordService(object):
	"""docstring"""
	@classmethod
	def all(cls):
		"""docstring"""
		return DBSession.query(Ban).order_by(sqlalchemy.desc(Ban.start_date))
	
	@classmethod
	def by_id(cls, id):
		"""docstring"""
		# The first method pulls the first item out of the list. Even though
		# there is only one item in the list, this is still necessary because it
		# is a list.
		return DBSession.query(Ban).filter(Ban.ban_id == id).first()
	
	# Bans are a type that should be paginated.
	
	# I really need to think about adding a parameter that represents how many
	# items appear on each page.
	@classmethod
	def get_paginator(cls, request, page=1):
		"""docstring"""
		query = DBSession.query(Ban).order_by(sqlalchemy.desc(Ban.start_date))
		query_params = request.GET.mixed()
		
		def url_maker(link_page):
			"""docstring"""
			query_params['page'] = link_page
			return request.current_route_url(_query=query_params)
		return SqlalchemyOrmPage(
			query,
			page,
			items_per_page=5,	# Adjust as needed
			url_maker=url_maker
		)
	
	# Create a list of current bans. These are bans whose end_date has not come
	# yet. I assume that we can just compare using less than and greater than
	# comparison operators.