import sqlalchemy
from paginate_sqlalchemy import SqlalchemyOrmPage	# For pagination purposes
from ..meta import DBSession
from ..topic import Topic

""" Post service docstring. """

class PostRecordService(object):
	""" This class retrieves posts from the database. """
	
	@classmethod
	def all(cls):
		""" This function retreives all of the posts ever made. """
		return DBSession.query(Post).order_by(sqlalchemy.desc(Post.start_date))
	
	@classmethod
	def by_id(cls, post_id):
		""" This function retreives a specific post. """
		return DBSession.query(Post).filter(Post.post_id == post_id).first()
	
	# Posts should be paginated.
	
	# Consider creating a parameter that represents how many items appear on
	# each page.
	@classmethod
	def get_paginator(cls, request, page=1):
		""" Get a subset of the posts that can be navigated. """
		# I think we can do this action by just calling all()
		# Also this should be adjusted so that we can get posts of a specific
		# context such as by user and by topic.
		query = DBSession.query(Post).order_by(sqlalchemy.desc(Post.start_date))
		
		query_params = request.GET.mixed()
		
		def url_maker(link_page):
			""" This function creates links to the various pages made. """
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
		""" Paginate posts made by a user. """
		# Get all the posts made by a user.
		query = DBSession.query(Post).filter(Post.user_id == user_id).order_by(
			sqlalchemy.desc(Post.start_date)
		)
		
		query_params = request.GET.mixed()
		
		def url_maker(link_page):
			""" This function creates links to the various pages made. """
			query_params['page'] = link_page
			return request.current_route_url(_query=query_params)
		return SqlalchemyOrmPage(
			query,
			page,
			items_per_page=5,
			url_maker
		)
	
	@classmethod
	def paginated_by_topic(cls, request, topic_id, page=1):
		""" Paginate posts made to a topic. """
		query = DBSession.query(Post).filter(Post.topic_id == topic_id).order_by(sqlalchemy.desc(Post.start_date))
		query_params = request.GET.mixed()
		
		# I actually could probably pull this out into a seperate function by
		# creaeing a function that returns a function.
		def url_maker(link_page):
			""" This function creates links to the various pages made. """
			query_params['page'] = link_page
			return request.current_route_url(_query=query_params)
		return SqlalchemyOrmPage(
			query,
			page,
			items_per_page=5,
			url_maker
		)
	
	# We have three pagination functions. It might be a better idea to create a 
	# single function that is used to paginate a query that gets passed.