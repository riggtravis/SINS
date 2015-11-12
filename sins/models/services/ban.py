import sqlalchemy
from paginate_sqlalchemy import SqlalchemyOrmPage	# For pagination purposes
from ..meta import DBSession
from ..topic import Topic

class BanRecordService(object):
	@classmethod
	def all(cls):
		return DBSession.query(Ban).order_by(sa.desc(Ban.start_date))
	
	@classmethod
	def by_id(cls, id):
		return DBSession.query(Ban).filter(Ban.ban_id == id).first()
	
	# Bans are a type that should be paginated.
	
	# I really need to think about adding a parameter that represents how many
	# items appear on each page.
	@classmethod
	def get_paginator(cls, request, page=1):
		query = DBSession.query(Ban).order_by(sa.desc(Ban.start_date))
		query_params = request.GET.mixed()
		
		def url_maker(link_page):
			query_params['page'] = link_page
			return request.current_route_url(_query=query_params)
		return SqlalchemyOrmPage(
			query,
			page,
			items_per_page=5,	# Adjust as needed
			url_maker=url_maker
		)