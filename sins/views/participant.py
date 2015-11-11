# I have chosen to include authentification/authorization views in the
# participant file. The reason I have chosen to do this is that it relates
# directly to users.

# Remember when constructing a profile that the avatar has to be passed
# seperately instead of as part of the user.
class ParticipantViews:
	def __init__(self, request):
		self.request = request
	
	# Show the participant's profile
	@view_config(route_name='user', renderer='sins:templates/profile.mako')
	def profile(self):
		# Search the database for a user whose id matches the user_id passed
		# through the URI 
		return {}
	
	# Let the participant log in and out.
	@view_config(
		route_name='auth',
		match_param='action=in',
		renderer='log.mako',
		request_method='POST'
	)
	@view_config(
		route_name='auth',
		match_param='action=out',
		renderer='log.mako'
	)
	def sign_in_out(self):
		# Make sure to pass a sign out message if the user is logging out.
		# The other thing to do is to pass what whether the user is logging in
		# or out so that there can be a sensible title like "success" or
		# "log in"
		return {}