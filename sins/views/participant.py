from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..models.meta import DBSession
from ..models.user import User
from ..models.services.user import UserRecordService
from ..models.services.post import PostRecordService

# I have chosen to include authentification/authorization views in the
# participant file. The reason I have chosen to do this is that it relates
# directly to users.
class ParticipantViews:
	def __init__(self, request):
		self.request = request
	
	# Show the participant's profile
	@view_config(route_name='user', renderer='sins:templates/profile.mako')
	def profile(self):
		# Search the database for a user whose id matches the user_id passed
		# through the URI.
		user_id = int(sef.request.matchdict.get('user_id', -1))
		user = UserRecordService.by_id(user_id) # Get the id from the URI.
		
		if user:
			# Don't forget that in order for pagination to work we need to
			# specify what page we want.
			paginated_posts = # Get paginated posts that were made by this user.
			return {'user': user, 'posts': paginated_posts}
		else:
			return HTTPNotFound()
	
	# Let the participant log in and out.
	@view_config(
		route_name='auth',
		match_param='action=in',
		renderer='sins:templates/log.mako',
		request_method='POST'
	)
	@view_config(
		route_name='auth',
		match_param='action=out',
		renderer='sins:templates/log.mako'
	)
	def sign_in_out(self):
		# Make sure to pass a sign out message if the user is logging out.
		# The other thing to do is to pass what whether the user is logging in
		# or out so that there can be a sensible title like "success" or
		# "log in"
		return {}