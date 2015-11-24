import sqlalchemy
from paginate_sqlalchemy import SqlalchemyOrmPage	# For pagination purposes
from ..meta import DBSession
from ..ban import Ban

# Get the url_maker function.
from .url_maker import url_maker

""" Ban service docstring. """

class BanRecordService(object):
	""" This class helps us get information about bans. """
	
	@classmethod
	def all(cls):
		""" Return all of the bans in the database. """
		return DBSession.query(Ban).order_by(sqlalchemy.desc(Ban.start_date))
	
	@classmethod
	def by_id(cls, id):
		""" Get a specific ban. """
		# The first method pulls the first item out of the list. Even though
		# there is only one item in the list, this is still necessary because it
		# is a list.
		return DBSession.query(Ban).filter(Ban.ban_id == id).first()
	
	# Bans are a type that should be paginated.
	
	# I really need to think about adding a parameter that represents how many
	# items appear on each page.
	@classmethod
	def get_paginator(cls, request, page=1):
		""" Make bans appear only a few at a time with a link to see more. """
		query = DBSession.query(Ban).order_by(sqlalchemy.desc(Ban.start_date))
		query_params = request.GET.mixed()
		
		# url_maker functions are defined everytime there is a get_paginator
		# function as a member of a class. There should be a way to create a
		# general use url maker that all of the classes use.
		def url_maker(link_page):
			""" This function lets the user have a way to change pages. """
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