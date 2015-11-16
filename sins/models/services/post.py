import sqlalchemy
from paginate_sqlalchemy import SqlalchemyOrmPage	# For pagination purposes
from ..meta import DBSession
from ..topic import Topic

class PostRecordService(object):
	@classmethod
	def all(cls):
		return DBSession.query(Post).order_by(sqlalchemy.desc(Post.start_date))
	
	@classmethod
	def by_id(cls, post_id):
		return DBSession.query(Post).filter(Post.post_id == post_id).first()
	
	# Posts should be paginated.
	
	# Consider creating a parameter that represents how many items appear on
	# each page.
	@classmethod
	def get_paginator(cls, request, page=1):
		# I think we can do this action by just calling all()
		query = DBSession.query(Post).order_by(sqlalchemy.desc(Post.start_date))
		
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
	
	# I need to figure out a way to get the paginaed posts from a single user.
	@classmethod
	def paginated_by_user(cls, request, user_id, page=1):
		# Get all the posts made by a user.
		query = DBSession.query(Post).filter(Post.user_id == user_id).order_py(sqlalchemy.desc(Post.start_date))
		
		query_params = request.GET.mixed()
		
		def url_maker(link_page):
			query_params['page'] = link_page
			return request.current_route_url(_query=query_params)
		return SqlalchemyOrmPage(
			query,
			page,
			items_per_page=5,
			url_maker
		)
	
	# We have two pagination functions. It might be a better idea to create a 
	# single function that is used to paginate a query that gets passed.