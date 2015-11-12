import sqlalchemy
from paginate_sqlalchemy import SqlalchemyOrmPage	# For pagination purposes
from ..meta import DBSession
from ..topic import Topic

class PostRecordService(object):
	@classmethod
	def all(cls):
		return DBSession.query(Post).order_by(sa.desc(Post.start_date))
	
	@classmethod
	def by_id(cls, id):
		return DBSession.query(Post).filter(Post.post_id == id).first()
	
	# Posts should be paginated.
	
	# Consider creating a parameter that represents how many items appear on
	# each page.
	@classmethod
	def get_paginator(cls, request, page=1):
		query = DBSession.query(Post).order_by(sa.desc(Post.start_date))
		query_params = request.GET.mixed()
		
		def url_maker(link_page):
			query_params['page'] = link_page
			return request.current_route_url(_query=query_params)
		return SqlalchemyOrmPage(
			query,
			page,
			items_per_page=5,	# Adjust as needed.
			url_maker=url_maker
		)