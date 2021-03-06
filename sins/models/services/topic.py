import sqlalchemy
from paginate_sqlalchemy import SqlalchemyOrmPage	# For pagination purposes
from ..meta import DBSession
from ..topic import Topic

""" Topic service

Classes:
* TopicRecordService
** This class provides methods for retrieving topics from the database.

"""

class TopicRecordService(object):
	""" This class retreives discussion topics from the database. """
	
	# There's a lot going on here that's new to me and I need to spend some time
	# reading the documentation.
	
	# The first thing I need to know is what this decorator does.
	# This decorator allows us to pass the class as a parameter instead of
	# passing an object of type TopicRecordService. I'm not clear on why we
	# would do this though. In fact truth be told, this looks like a place where
	# a static method decorator would make more sense because there's no
	# reference to cls in the function itself.
	@classmethod
	def all(cls):
		""" This function retreives all of the Topics. """
		# I need to look at what DBSession's type is so that I can know what
		# methods it has. They I need to read about those methods so that I can
		# know precisely what they do. There's a solid chance that I will want
		# to use some of the functionalities in other service helpers.
		
		# DBSession = 
		#	scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
		
		# The scoped_session function comes from sqlalchemy.orm, so now I'm
		# going to look into this function.
		
		# The sessionmaker function creates an object of type Session which is
		# used to make queries to the database. It seems pretty clear to me that
		# scoped_session in some way gives DBSession some sort of session from
		# the sessionmaker function. However, what does not make sense to me is
		# is why this is necessary. Interestingly the documentation for 
		# sessionmaker uses sessionmaker to bind sessions to a particular
		# database engine. However, this isn't happening with our call to
		# sessionmaker. I think it might be possible that the scoped_session
		# function call is what is doing that binding.
		
		# Sessions are kept at the global level. I hadn't noticed before, but
		# DBSession is a global variable. This means that its name should
		# probably be in all caps. I will worry about such trifles after this
		# application is ready for its first public release.
		
		# scoped_session creates a registry of Session objects. This means that
		# we can safely interact with the DBSession object without worrying too
		# much about unintentional interactions. This is just one way to manage
		# databases in SQLalchemy, but it probably what I am going to stick to
		# since it is well documented by the pyramid project.
		return DBSession.query(Topic).order_by(sqlalchemy.desc(Topic.start_date))
	
	# Search topics by the id.
	@classmethod
	def by_id(cls, id):
		""" This function retreives a specific topic. """
		# I don't understand why we need to tell the query how to sort the
		# topics. Primary keys are unique.
		return DBSession.query(Topic).filter(Topic.topic_id == id).first()
	
	# Now, we make the paginating happen (it shall be glorious)
	# Okay, this is a little curious. I need to know why one of the arguments
	# get_paginator has a value set. Maybe that's how you do default values for
	# parameters in Python. This is indeed how you do default values for
	# arguments in Python. This may come in handy later.
	
	# It may be worth considering adding a parameter that represents how many
	# items appear on each page.
	@classmethod
	def get_paginator(cls, request, page=1):
		""" This function creates a paginated display of topics. """
		query = DBSession.query(Topic).order_by(sqlalchemy.desc(
				Topic.start_date
			)
		)
		
		# I can't find documentation for this action.
		# I got the command from this tutorial on how to build a web app:
		# http://pyramid-blogr.readthedocs.org/en/latest/blog_models_and_views.html
		query_params = request.GET.mixed()
		
		# Get ready to do something crazy. We are about to define a function
		# within a function. We can do this because functions are first class
		# citizens in Python. The syntax we are about to use was originally
		# conceived (or more correctly, allowed) in order to create clojures in
		# which a function returns a function that is based on another function.
		# (Whaaaaaaaaaaaaaaaat?) Think of functions in Python not as things
		# seperate from data that manipulate date. More correctly they are data
		# that manipulates data.
		
		# But here's the kicker. We're not going to use this syntax to create a
		# clojure. We're going to be making what is in essence a lambda
		# function. Lambdas are functions that are one time use only, so they
		# are not placed in a scope where other fuctions can access them.
		# Usually they can be represented as a single line, and are defined in
		# in the same line of code as they are used. We're cheating a bit and 
		# creating a multiline lambda by using a full function definition and
		# then using that function in the next line afterwards. But since this
		# is the only time we will need our function, we only define it in the
		# scope of the get_paginator function.
		def url_maker(link_page):
			""" This function allows us to have links to the pages made. """
			# Replace the page parameter with values generated by paginator
			query_params['page'] = link_page
			
			return request.current_route_url(_query=query_params)
		return SqlalchemyOrmPage(
			query, 
			page, 
			items_per_page=5,	# Adjust as needed.
			url_maker=url_maker
		)
	
	def paginated_by_user(cls, request, user_id, page=1):
		""" This function creates a paginated display of a user's topics. """
		query = DBSession.query(Topic).filter(Topic.user_id == user_id).order_by(sqlalchemy.desc(Topic.start_date))
		query_params = request.GET.mixed()
		
		def url_maker(link_page):
			""" This function allows us to have links to the pages made. """
			query_params['page'] = link_page
			return request.current_route_url(_query=query_params)
		return SqlalchemyOrmPage(
			query,
			page,
			items_per_page=5,
			url_maker=url_maker
		)
	
	def paginated_by_forum(cls, request, forum_id, page=1):
		""" This function creates a paginated display of topic in a forum. """
		query = DBSession.query(Topic).filter(Topic.forum_id == forum_id).order_by(sqlalchemy.desc(Topic.start_date))
		query_params = request.GET.mixed()
		
		def url_maker(link_page):
			""" This function allows us to have links to the pages made. """
			query_params['page'] = link_page
			return request.current_route_url(_query=query_params)
		return SqlalchemyOrmPage(
			query,
			page,
			items_per_page=5,
			url_maker=url_maker
		)